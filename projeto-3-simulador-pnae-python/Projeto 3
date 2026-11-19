### Parâmetros ###
# Valores per capita por dia letivo (Resolução CD/FNDE nº 1/2026)
valCreche = 1.57
valPreEscola = 0.82
valFundamental = 0.57

# Limites de porte da escola (total de matrículas) - conferir com o Projeto 1
LIMITE_MICRO = 50
LIMITE_PEQUENA = 200

# Custo dos alimentos de uma refeição escolar (R$)
# Fonte: "Análise dos gastos reais x repasse de verbas para a alimentação escolar de duas
# escolas estaduais do interior do estado de São Paulo" - custo médio de matéria-prima por
# refeição, dados de ago-nov/2023. https://static.even3.com/anais/1072522.pdf
CUSTO_ALIMENTOS_REFEICAO = 3.60


### Funções (processo do backend) ###
def ler_numero(mensagem):
    numero = input(mensagem)
    while not numero.isdigit():
        print("Você digitou um número inválido. Digite apenas números inteiros.")
        numero = input(mensagem)
    numero = int(numero)
    return numero


def classificar_porte(numMatriculas):
    if numMatriculas <= LIMITE_MICRO:
        porteEscola = "Micro"
    elif numMatriculas <= LIMITE_PEQUENA:
        porteEscola = "Pequena"
    else:
        porteEscola = "Média"
    return porteEscola


def calcular_repasse(qtdeMatriculas, valUnitario, dias):
    totalRepasse = qtdeMatriculas * valUnitario * dias
    return totalRepasse


def calcular_custo_alimentos(totAlunos, dias, custoRefeicao):
    # uma refeição por aluno por dia letivo
    custoAnual = totAlunos * dias * custoRefeicao
    return custoAnual


def calcular_cobertura(repasse, custoAnual):
    if custoAnual == 0:
        # escola sem alunos: não há custo a cobrir
        return 0, 0, True
    cobertura = repasse / custoAnual * 100
    if repasse >= custoAnual:
        diferenca = 0
        cobre = True
    else:
        diferenca = custoAnual - repasse
        cobre = False
    return cobertura, diferenca, cobre


def formatar_reais(valor):
    # 37660.0 -> "R$ 37.660,00"
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return "R$ " + texto


### Programa Principal ###
print("Olá, bem-vindo ao simulador PNAE")
nome = input("Digite o seu nome: ")
escola = input("Digite o nome da sua escola: ")

## pedir dias letivos
diasLetivos = ler_numero("Qual a quantidade de dias letivos do ano: ")

## pedir as matrículas
print("Digitação das Matrículas (digite 0 se a escola não tiver a etapa)")
creche = ler_numero("Digite as matrículas na creche: ")
preEscola = ler_numero("Digite as matrículas na pré-escola: ")
fundamental = ler_numero("Digite as matrículas no fundamental: ")

totMatriculas = creche + preEscola + fundamental

repasseCreche = calcular_repasse(creche, valCreche, diasLetivos)
repassePreEscola = calcular_repasse(preEscola, valPreEscola, diasLetivos)
repasseFundamental = calcular_repasse(fundamental, valFundamental, diasLetivos)

repasseTotal = repasseCreche + repassePreEscola + repasseFundamental

porte = classificar_porte(totMatriculas)

custoAnual = calcular_custo_alimentos(totMatriculas, diasLetivos, CUSTO_ALIMENTOS_REFEICAO)
cobertura, diferenca, cobre = calcular_cobertura(repasseTotal, custoAnual)

## Montando a tela com resultados
print()
print("=== Cálculos ===")
print("Usuário:", nome)
print("Escola:", escola)
print("Total de matrículas:", totMatriculas)
print("Porte da escola:", porte)
print()
print("Valor a receber Creche:", formatar_reais(repasseCreche))
print("Valor a receber Pré-Escola:", formatar_reais(repassePreEscola))
print("Valor a receber Fundamental:", formatar_reais(repasseFundamental))
print("Valor a receber Total:", formatar_reais(repasseTotal))
print()
print("=== Cobertura do repasse ===")
print("Custo dos alimentos por refeição:", formatar_reais(CUSTO_ALIMENTOS_REFEICAO))
print("Custo anual estimado dos alimentos:", formatar_reais(custoAnual))
print(f"Cobertura do repasse federal: {cobertura:.1f}%".replace(".", ","))
print("Diferença a ser coberta por outras fontes:", formatar_reais(diferenca))
if cobre:
    print("O repasse federal cobre o custo estimado dos alimentos.")
else:
    print("O repasse federal NÃO cobre o custo estimado dos alimentos.")
print("---- Fim dos Cálculos ----")
print()
input("Digite Enter para sair")
