Projeto 1 — Simulador de Repasse do PNAE

Objetivo: o projeto calcula o repasse anual estimado do PNAE (Programa Nacional de Alimentação Escolar) para uma escola, a partir do número de matrículas por modalidade de ensino e dos valores per capita oficiais. Ele também classifica o porte da escola, aplica uma regra de elegibilidade para complementação municipal e simula como o repasse varia sob diferentes cenários de aumento ou queda nas matrículas (fator de ajuste).

Como usar:

Abra Projeto_1_-_Tabela_de_Dados.xlsx para ver o modelo original: a aba Parametros_PNAE traz os valores per capita e as faixas de porte; a aba Simulador_Escola traz os dados da escola, a tabela de matrículas, o cálculo do repasse e a Tabela de Dados com os cenários.

Abra simulador_pnae.html em qualquer navegador (não precisa de internet) para usar a versão interativa do mesmo modelo.
No simulador, preencha o número de matrículas por modalidade no topo — todos os resultados (total, porte, repasse, elegibilidade) recalculam automaticamente.

Use o campo "Fator de ajuste" para ver matrículas e repasse mudarem em tempo real.
Na seção de cenários, clique em "Calcular próximo cenário" para reconstruir, passo a passo, a mesma Tabela de Dados da planilha (variação de −20% a +20%).

Uso de Inteligência Artificial

Ferramenta utilizada: Claude (Anthropic), modelo Sonnet, no aplicativo web claude.ai.
Para que foi usada: gerar o artefato HTML interativo do simulador (simulador_pnae.html) a partir do modelo já construído em Excel, reproduzindo fielmente os dados, faixas de classificação e fórmulas da planilha (SOMA, PROCV, SOMARPRODUTO, SE aninhado com E/OU e o fator de ajuste da Tabela de Dados) em uma interface web com campos editáveis e um mecanismo de avanço passo a passo pelos cenários.

Exemplo de prompt utilizado:
"Você vai gerar um artefato HTML interativo (um único arquivo, autocontido) que simula o cálculo do repasse do PNAE, a partir do modelo que eu construi em Excel para o Projeto 1 do curso Análise de Dados para Pesquisas em Políticas Públicas (FGV EAESP). Anexei dois arquivos: 1) Minha planilha Excel, com as abas Parametros_PNAE e Simulador_Escola, contendo os dados e as fórmulas. 2) Um arquivo modelo.html, [...] usado apenas como referência de paleta de cores e tipografia, formato dos cards e das tabelas, e o tipo de mecânica interativa [...]. Use os dados reais da minha planilha [...]. Não invente números nem modalidades que não estejam na minha planilha. Reproduza as fórmulas da minha planilha com a mesma lógica [...] não simplifique nem troque por uma lógica diferente da que eu construí."

O que foi ajustado manualmente: os valores gerados pela IA (matrículas base, valores per capita, total, porte, repasse e os 9 cenários da Tabela de Dados) foram conferidos célula a célula contra os valores em cache da planilha original antes da entrega. Além disso, ajustamos manualmente o texto de introdução do simulador para deixá-lo mais direto, reduzimos o tamanho das fontes dos cards de resultado para caber melhor em tela menor, corrigimos o arredondamento exibido nas matrículas ajustadas (que estava aparecendo com duas casas decimais desnecessárias) e revisamos as células citadas na lista final do artefato para garantir que cada referência (Parametros_PNAE!..., Simulador_Escola!...) apontasse exatamente para a célula certa da planilha.

Fonte de Dados

Fonte oficial: Resolução CD/FNDE nº 1, de 18 de fevereiro de 2026, que altera a Resolução CD/FNDE nº 6/2020 e reajusta em 14,35%, em média, os valores per capita do PNAE para 2026.

Link oficial: https://www.gov.br/fnde/pt-br/acesso-a-informacao/acoes-e-programas/programas/pnae
O que os dados representam: os valores per capita diários (R$/dia por aluno) que o FNDE repassa a estados e municípios para a alimentação escolar, diferenciados por modalidade de ensino (creche, pré-escola, fundamental, médio, EJA, educação indígena/quilombola e AEE), além do número de dias letivos considerados no cálculo anual (200 dias). Os dados de matrículas por modalidade e o nome/bairro/município da escola são fictícios, criados para fins didáticos do exercício.

Estrutura:

Coluna/variável	O que significa
Modalidade (Parametros_PNAE)	Etapa/modalidade de ensino atendida pelo PNAE

Valor per capita (R$/dia)	Valor repassado por aluno/dia naquela modalidade

Dias letivos (ano)	Número de dias letivos usados no cálculo do repasse anual (200)

Matrículas (mínimo) / Porte	Faixas usadas para classificar a escola como Pequena, Média ou Grande

Matrículas (Simulador_Escola)	Número de alunos matriculados por modalidade na escola simulada

Fator de Ajuste	Percentual de variação aplicado às matrículas para simular cenários de crescimento/queda

Participação do Grupo
O que aprendemos com este projeto: aprendemos a estruturar um modelo de cálculo de política pública em planilha combinando funções como PROCV, SOMARPRODUTO e SE aninhado com E/OU, e a usar a Tabela de Dados do Excel (Dados/Teste de Hipótese) para testar cenários de forma sistemática, sem precisar recalcular manualmente cada variação. Também aprendemos a traduzir a lógica e as fórmulas de uma planilha para uma ferramenta interativa, mantendo a fidelidade dos cálculos ao sair do Excel para o HTML, e a documentar de forma transparente onde e como usamos IA no processo.

Papel de cada integrante:
João Henrique Viana: estruturou o modelo no Excel (abas Parametros_PNAE e Simulador_Escola), definiu as fórmulas de cálculo do repasse, da classificação de porte e da regra de elegibilidade, e conduziu a geração e a conferência do artefato HTML interativo com apoio de IA.

Gustavo Del Gilgio: levantou e organizou os parâmetros oficiais do PNAE (valores per capita e regras da Resolução CD/FNDE nº 1/2026), e ajudou a validar se os resultados do simulador batiam com os valores calculados manualmente.

João Vitor Arantes: construiu a Tabela de Dados (What-If Analysis) com os cenários de variação do fator de ajuste, testou o simulador HTML em diferentes combinações de matrículas e revisou a redação final do README.
