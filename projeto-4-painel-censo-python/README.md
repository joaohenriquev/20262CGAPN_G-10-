# Projeto 4 — Painel Interativo do Censo Escolar em Python

**Objetivo:** o painel mostra as escolas em atividade de 30 municípios de quatro regiões do estado de São Paulo (Região Metropolitana, Baixada Santista, Litoral Norte e Vale do Ribeira), com dados do Censo Escolar 2024. Com os filtros, dá para comparar regiões, redes de ensino e municípios quanto ao número de escolas e de matrículas, ao porte e à localização das escolas, à infraestrutura de água e esgoto, e ver cada escola no mapa. Pode ser usado, por exemplo, para identificar onde estão as escolas com infraestrutura mais precária.

## Como usar

**1. Instalar os pacotes** (só na primeira vez). No terminal, digite:

```
python -m pip install pandas streamlit
```

(no Mac, pode ser preciso trocar `python` por `python3` em todos os comandos)

**2. Rodar o painel.** No terminal, entre na pasta deste projeto, onde estão o `painel.py` e a base `escolas_sp_regioes_2024_geo.csv`, e digite:

```
python -m streamlit run painel.py
```

O painel abre sozinho no navegador. Para fechar, volte ao terminal e aperte `Control + C`.

**3. Usar os filtros.** Os filtros ficam na barra lateral, à esquerda. Escolha uma opção em cada um, e o painel inteiro é recalculado na hora: indicadores, gráficos, mapa e lista. Os filtros se somam. Por exemplo, "Vale do Ribeira" + "Municipal" mostra só as escolas municipais do Vale do Ribeira. A lista do filtro de município mostra apenas os municípios que sobram depois dos filtros de região e dependência. Para voltar a ver todas as escolas, escolha "Todas" ou "Todos".

## Prints do resultado

Painel com todas as regiões e todas as redes:

![Painel com todas as regiões](prints/painel_todas.png)

Painel com o Vale do Ribeira selecionado:

![Painel com o Vale do Ribeira](prints/painel_vale.png)

## Elementos do painel

| Tipo | Elemento | Coluna da base usada |
|---|---|---|
| Indicador | Total de escolas | contagem de linhas (cada linha é uma escola) |
| Indicador | Total de matrículas | `matriculas` (soma) |
| Filtro | Região | `regiao` |
| Filtro | Dependência administrativa | `dependencia` |
| Filtro | Município | `municipio` |
| Gráfico de característica | Escolas por porte | `porte` (criada a partir de `matriculas` com a função `classificar_porte`) |
| Gráfico de característica | Escolas por localização | `localizacao` |
| Gráfico de infraestrutura | Escolas por abastecimento de água | `agua` |
| Gráfico de infraestrutura | Escolas por esgotamento sanitário | `esgoto` |
| Mapa | Mapa das escolas | `latitude` e `longitude` |
| Lista | Lista das escolas | `municipio`, `escola`, `dependencia`, `localizacao`, `matriculas` e `porte` |

Os dois gráficos de características usam colunas que não estão nos filtros (`porte` e `localizacao`).

O porte segue a mesma regra vista em aula: **Pequena** até 200 matrículas, **Média** de 201 a 400 e **Grande** acima de 400.

## O que o painel mostra

A diferença mais visível entre as regiões está no abastecimento de água. Quando se seleciona o Vale do Ribeira, o painel mostra 338 escolas e 63.777 matrículas. Dessas escolas, 265 recebem água da rede pública, mas 73 (cerca de 22%) dependem de outras fontes: 28 usam fonte ou rio, 27 usam cacimba, 17 usam poço artesiano e 1 não tem abastecimento de água. Já na Região Metropolitana de SP, 1.261 das 1.263 escolas recebem água da rede pública (99,8%), e na Baixada Santista são 1.172 de 1.189 (98,6%). O esgoto segue o mesmo padrão: no Vale, 75 escolas (22%) não estão ligadas à rede pública e 3 não têm esgotamento nenhum, contra apenas 10 escolas na Região Metropolitana. Parte da explicação aparece no gráfico de localização: 124 das 338 escolas do Vale do Ribeira (37%) são rurais, contra só 2 na Região Metropolitana. Ou seja, a infraestrutura básica das escolas também acompanha a desigualdade entre regiões do estado. O mapa ajuda a ver onde estão essas escolas, e o filtro de município mostra em quais cidades do Vale o problema se concentra.

## Organização do programa

O arquivo `painel.py` segue a ordem vista em aula: a função primeiro, depois o carregamento dos dados e, por fim, os comandos que montam o painel, com os filtros antes dos indicadores e dos gráficos. Como cada filtro reduz a tabela `censo` antes de qualquer cálculo, todos os elementos que vêm depois respondem aos filtros.

| Parte do código | O que faz | Elemento correspondente no painel do Projeto 2 (Excel) |
|---|---|---|
| Função `classificar_porte` | Classifica a escola como Pequena, Média ou Grande pelo número de matrículas | Coluna calculada de porte, com a fórmula `SE` |
| Carregamento dos dados (`pd.read_csv`) e criação da coluna `porte` | Lê a base do Censo e acrescenta o porte de cada escola | Importação da base do Censo para a planilha (Power Query) |
| Filtros (`st.sidebar.selectbox` + `censo[...]`) | Mantêm só as escolas da região, da dependência e do município escolhidos | Segmentação de dados |
| Indicadores (`st.metric`) | Mostram o total de escolas e o total de matrículas | Big numbers do dash (cartões com totais) |
| Gráficos (`value_counts` + `st.bar_chart`) | Contam as escolas por porte, localização, água e esgoto | Tabelas dinâmicas e gráficos dinâmicos |
| Mapa (`st.map`) | Mostra cada escola como um ponto, pela latitude e longitude | Sem correspondência (novo no Projeto 4) |
| Lista (`st.dataframe`) | Mostra as escolas que atendem aos filtros | Tabela com a lista de escolas filtrada |

## Uso de Inteligência Artificial

**Ferramenta utilizada:** Claude (Anthropic)

**Para que foi usada:** para conferir o painel da Aula 21 com as orientações do Projeto 4, acrescentar os filtros de dependência e município e os novos gráficos de localização e esgoto, e montar um rascunho deste README.

**Exemplo de prompt utilizado:** enviamos o painel da Aula 21, o script de revisão, o notebook da Aula 20 e o documento de orientações do Projeto 4, e escrevemos: "Vamos para o projeto 4".

**O que foi ajustado manualmente:** rodamos o painel com a base real e testamos várias combinações de filtros para conferir que indicadores, gráficos, mapa e lista mudavam juntos. Também tiramos os prints e conferimos os números do Vale do Ribeira citados no README com o painel e com o notebook da Aula 20. A IA também apontou dois erros do código da aula, que corrigimos: a primeira linha do arquivo, que era texto sem `#` e impedia o painel de rodar, e o porte, que estava em minúsculas.

## Fonte de Dados

**Fonte oficial:** Censo Escolar 2024 (INEP)

**Link oficial:** https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar

**O que os dados representam:** o Censo Escolar é o levantamento anual do INEP com todas as escolas de educação básica do Brasil. A base usada aqui é um recorte preparado para o curso, `escolas_sp_regioes_2024_geo.csv`, com as escolas em atividade de 30 municípios de quatro regiões do estado de São Paulo. Cada linha é uma escola, com suas características, matrículas, infraestrutura e coordenadas geográficas.

**Estrutura (colunas usadas no painel):**

| Coluna | O que significa |
|---|---|
| `regiao` | Região do estado: Região Metropolitana de SP, Baixada Santista, Litoral Norte ou Vale do Ribeira |
| `municipio` | Município da escola |
| `escola` | Nome da escola |
| `dependencia` | Rede de ensino: Federal, Estadual, Municipal ou Privada |
| `localizacao` | Urbana ou Rural |
| `matriculas` | Total de matrículas da escola |
| `agua` | Principal forma de abastecimento de água |
| `esgoto` | Principal forma de esgotamento sanitário |
| `latitude` e `longitude` | Coordenadas da escola, usadas no mapa |
| `porte` | Não vem na base: é criada no programa a partir de `matriculas` |

## Participação do Grupo

**O que aprendemos com este projeto:** aprendemos a refazer em Python o painel que tínhamos construído em Excel no Projeto 2. Com o pandas, carregamos, filtramos e contamos os dados, e com o Streamlit transformamos um script em uma página interativa. Entendemos que a segmentação de dados do Excel equivale a filtrar a tabela antes de calcular qualquer coisa, e que a ordem do código importa. Também vimos que um painel bem montado mostra rapidamente desigualdades que passam despercebidas numa tabela, como a diferença de acesso à água entre as escolas do Vale do Ribeira e as das regiões mais urbanizadas.

**Papel de cada integrante:**
- **João Henrique Viana:** escolheu a versão do painel da Aula 21 usada pelo grupo, corrigiu os erros do código e acrescentou os filtros de dependência e município.
- **Gustavo Del Gilgio:** usou o `value_counts()` para conferir os valores das colunas, escolheu os novos gráficos (localização e esgoto), testou as combinações de filtros e tirou os prints.
- **João Vitor Arantes:** escreveu a análise "O que o painel mostra", organizou a pasta no GitHub e redigiu o README.
