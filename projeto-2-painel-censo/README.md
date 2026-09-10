Projeto 2 — Infraestrutura Básica das Escolas de São Paulo (Água, Energia, Esgoto e Lixo)

Objetivo: o projeto analisa a infraestrutura básica das escolas de educação básica do município de São Paulo — abastecimento de água, energia elétrica, esgotamento sanitário e destinação do lixo — a partir dos microdados do Censo Escolar 2024. Por meio de tabelas dinâmicas, ele mostra quantas escolas dependem de rede pública em cada um dos quatro serviços e quantas recorrem a soluções alternativas, precárias ou não informam a situação (escolas inativas).

Como usar:

Abra João_Henrique_Projeto_2_com_Dinamicas.xlsx.
Vá até a aba DINÂMICAS: nela já estão as seis tabelas dinâmicas do projeto — as duas originais (Dependência administrativa e Porte da escola) e as quatro novas (Água, Energia, Esgoto e Lixo).

Se quiser atualizar os valores após qualquer alteração na base, clique em qualquer uma das tabelas e use Analisar Tabela Dinâmica → Atualizar.

A aba microdados_ed_basica_2024 traz a base bruta (uma linha por escola); a aba Parâmetros documenta os códigos numéricos usados nas variáveis categóricas; a aba Água-Energia-Esgoto-Lixo traz o dicionário dos indicadores de infraestrutura.
Uso de Inteligência Artificial

Ferramenta utilizada: Claude (Anthropic), modelo Sonnet, no aplicativo web claude.ai.

Para que foi usada: primeiro, para sugerir ideias de cruzamentos de tabela dinâmica a partir das colunas de água, esgoto, energia e lixo presentes nos microdados; depois, para efetivamente construir quatro tabelas dinâmicas nativas do Excel (uma para cada tema) dentro do arquivo .xlsx, incluindo os caches de dados que as sustentam.

Exemplo de prompt utilizado:
"Faca na verdade um de cada e não um com vários, então: uma tabela para esgoto, outra para energia, outra para agua e outra para lixo"

O que foi ajustado manualmente: conferimos se os totais de cada tabela batiam com o total de escolas da base (8.023), comparamos os valores gerados com uma contagem manual das mesmas colunas na planilha, testamos a abertura do arquivo em outro programa de planilhas para garantir que não ficou corrompido, e reorganizamos a posição das quatro tabelas na aba DINÂMICAS para não sobrepor os gráficos e as tabelas dinâmicas que já existiam ali.

Fonte de Dados

Fonte oficial: Censo Escolar da Educação Básica 2024 (INEP/MEC).

Link oficial: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar
O que os dados representam: o Censo Escolar é o principal levantamento estatístico da educação básica brasileira, coletado anualmente pelo INEP junto a todas as escolas públicas e privadas do país. Os microdados usados neste projeto trazem, para cada escola do município de São Paulo, informações de localização, dependência administrativa, porte, número de matrículas e a infraestrutura disponível de água, energia, esgoto e destinação do lixo.

Estrutura:
Coluna/variável	O que significa

NO_ENTIDADE / NO_MUNICIPIO	Nome da escola e do município

DEPENDENCIA	Dependência administrativa (Estadual, Municipal, Federal, Privada)

LOCALIZAÇÃO	Zona urbana ou rural

TAM_ESCOLA	Porte da escola (Microescola a Mega escola), calculado a partir do total de matrículas

ABAST_AGUA / ENERGIA / ESGOTO	Tipo principal de abastecimento/escoamento de cada serviço (ex.: rede pública, poço artesiano, fossa séptica)

LIXO	Situação da destinação do lixo (sim, não, ou inativa)

IN_AGUA_*, IN_ENERGIA_*, IN_ESGOTO_*, IN_LIXO_*	Indicadores binários (0/1) que detalham cada solução específica dentro de cada serviço

QT_MAT_BAS	Total de matrículas na educação básica, usado para classificar o porte da escola

Participação do Grupo

O que aprendemos com este projeto: aprendemos a trabalhar com uma base de microdados grande e "crua" (mais de 8 mil linhas e 63 colunas), filtrando e organizando apenas as variáveis relevantes para a pergunta de pesquisa. Também aprendemos a construir tabelas dinâmicas de forma independente para cada tema, evitando misturar demais variáveis em uma única tabela, e a interpretar indicadores binários (0/1) de infraestrutura como proxy de precariedade ou vulnerabilidade de uma escola. Por fim, aprendemos a documentar com transparência onde e como usamos IA para gerar partes técnicas do arquivo, sem perder o controle sobre a conferência dos resultados.

Papel de cada integrante:
João Henrique Viana: organizou a base de microdados do Censo Escolar 2024, definiu quais indicadores de água, esgoto, energia e lixo seriam analisados, e conduziu a geração das tabelas dinâmicas com apoio de IA, incluindo a conferência final dos totais.

Gustavo Del Gilgio: pesquisou a documentação oficial do Censo Escolar e do dicionário de variáveis do INEP, ajudou a interpretar os códigos das colunas categóricas na aba Parâmetros e revisou se as classificações (ex.: porte da escola) estavam de acordo com a metodologia oficial.

João Vitor Arantes: testou as quatro tabelas dinâmicas com diferentes cruzamentos (ex.: água por dependência administrativa), validou se os números batiam com contagens manuais em uma amostra da base, e redigiu a documentação final do projeto.
