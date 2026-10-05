# Projeto 2 (atualizado) — Painel do Censo Escolar 2024 com Power Query

**Objetivo:** o painel mostra a infraestrutura básica (água, energia, esgoto e lixo), a dependência administrativa, a localização e o porte das escolas de **um município escolhido pelo grupo**, a partir da base completa do Censo Escolar 2024. As tabelas dinâmicas, os gráficos, a segmentação e o dashboard se alimentam de uma tabela tratada pelo Power Query, que filtra o município informado.

**O que mudou em relação à versão anterior:** a versão anterior trabalhava com um recorte já pronto das escolas de São Paulo (8.023 escolas), tratado com fórmulas na própria planilha. Agora a planilha importa a **base nacional completa** (todos os municípios do Brasil) via Power Query, e o **filtro é feito dentro do Power Query**, por um Merge com Junção Interna (UF + Município) com a tabela da aba `Digite_Municipio`. Assim, as dinâmicas só processam o município escolhido, mesmo com a base tendo centenas de milhares de linhas. As colunas derivadas (Dependência, Localização, Localização Diferenciada, Situação, Tamanho da Escola e os indicadores de Água, Energia, Esgoto e Lixo), antes feitas com PROCV/SE/SES, agora são criadas no Power Query (Merges Esquerda Externa e colunas condicionais).

**Como usar:**
1. Salve o arquivo `Censo_2024_Excel.xlsx` (base nacional, disponibilizada no eClass) na pasta **Downloads** e abra `Projeto2_Painel_Censo_PowerQuery_LEVE.xlsx`.
2. Na aba `Digite_Municipio`, informe a **UF** e o **Município**, exatamente como aparecem na base (ex.: SP e São Paulo).
3. Clique em **Dados → Atualizar Tudo** e aguarde o Power Query terminar.
4. Veja o resultado na aba `DINÂMICAS` e no dashboard.
5. As consultas ficam em **Dados → Consultas e Conexões** (`Filtro`, `Dependencia`, `Localizacao`, `LocDiferenciada`, `Situacao`, `BaseBrasil` e `CensoEscolar`). O código de cada uma está em **Editor Avançado**.

**Estrutura das consultas:** `BaseBrasil` só abre o arquivo do Censo e fica como "somente conexão"; `CensoEscolar` faz o Merge Interno com `Filtro`, os quatro Merges Esquerda Externa com as tabelas auxiliares e cria as colunas condicionais. Separamos `BaseBrasil` de `CensoEscolar` para evitar o erro de nível de privacidade do Excel, que aparece quando uma mesma consulta abre um arquivo e usa outras consultas. O caminho do arquivo do Censo está escrito dentro da consulta `BaseBrasil` e precisa ser ajustado se o arquivo estiver em outra pasta.

---

## Uso de Inteligência Artificial

**Ferramenta utilizada:** Claude (Anthropic), no aplicativo web claude.ai.

**Para que foi usada:** o Claude nos ajudou a entender e montar o README do projeto, explicando passo a passo o que cada seção deveria conter. Também foi usado para sugerir e construir as tabelas dinâmicas de Água, Energia, Esgoto e Lixo, para escrever o código do Power Query e para nos orientar, passo a passo, na montagem das consultas e na correção dos erros.

**Exemplo de prompt utilizado:**
> "Me explique, passo a passo e de forma simples, como fazer o README do meu projeto, com objetivo, como usar e os disclaimers."

**O que foi ajustado manualmente:** todos os resultados foram conferidos pelo grupo, que criou as consultas no Excel, colou o código, ajustou os nomes das tabelas e das consultas, separou a consulta `BaseBrasil` da `CensoEscolar` e reapontou as tabelas dinâmicas para a nova base.

---

## Fonte de Dados

**Fonte oficial:** Censo Escolar da Educação Básica 2024 (INEP/MEC).

**Link oficial:** https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar

**O que os dados representam:** o Censo Escolar é um levantamento anual respondido por todas as escolas públicas e privadas do país. A base usada no projeto é um arquivo em Excel com os microdados do Censo, disponibilizado pela professora no eClass. Cada linha é uma escola, com localização, dependência administrativa, situação de funcionamento, matrículas e indicadores de infraestrutura de água, energia, esgoto e lixo.

**Aviso:** os dados são oficiais, mas as classificações de Água, Energia, Esgoto, Lixo e Tamanho da Escola foram criadas por nós, a partir de regras de prioridade e de faixas de matrículas. Escolas inativas aparecem com campos de infraestrutura em branco. Os números do painel servem para estudo e podem diferir de publicações oficiais do INEP.

**Estrutura:**
| Coluna/variável | O que significa |
|---|---|
| `SG_UF`, `NO_MUNICIPIO` | UF e município da escola (chaves do filtro) |
| `TP_DEPENDENCIA` → `DEPENDENCIA` | Federal, Estadual, Municipal ou Privada (tabela auxiliar) |
| `TP_LOCALIZACAO` → `LOCALIZAÇÃO` | Urbana ou Rural (tabela auxiliar) |
| `TP_LOCALIZACAO_DIFERENCIADA` → `LOC_DIFERENCIADA` | Assentamento, terra indígena, quilombola, etc. (tabela auxiliar) |
| `TP_SITUACAO_FUNCIONAMENTO` → `SITUAÇÃO` | Ativa ou Inativa (tabela auxiliar) |
| `IN_AGUA_*`, `IN_ENERGIA_*`, `IN_ESGOTO_*`, `IN_LIXO_*` | Indicadores 0/1 de cada solução de infraestrutura |
| `ABAST_AGUA`, `ENERGIA`, `ESGOTO`, `LIXO` | Colunas condicionais: a primeira opção marcada com 1, na ordem de prioridade |
| `QT_MAT_BAS` → `TAM_ESCOLA` | Matrículas e porte (Microescola a Mega escola) |

---

## Participação do Grupo

**O que aprendemos com este projeto:** o projeto nos mostrou que filtrar os dados antes de carregá-los no Excel é o que permite trabalhar com a base nacional do Censo Escolar, com mais de 200 mil escolas, sem travar a planilha. Aprendemos a diferença entre a junção interna, que filtra, e a junção esquerda externa, que enriquece, e a recriar fórmulas de planilha como colunas condicionais no Power Query. Também aprendemos a ler as mensagens de erro do Excel e a corrigir as consultas a partir delas.

**Papel de cada integrante:**
- **João Henrique Viana:** montou a aba onde se informa a UF e o município (`Digite_Municipio`), criou a consulta principal com a junção interna que reduz a base ao município escolhido e reapontou as tabelas dinâmicas para a nova base.
- **Gustavo Del Gilgio:** importou as tabelas auxiliares de Dependência, Localização, Localização Diferenciada e Situação, fez as junções esquerdas externas e conferiu as descrições trazidas.
- **João Vitor Arantes:** criou as colunas condicionais de Tamanho da Escola, Água, Energia, Esgoto e Lixo, conferiu os totais das tabelas dinâmicas e montou o dashboard.
