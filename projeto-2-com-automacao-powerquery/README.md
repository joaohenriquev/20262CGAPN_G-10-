# Projeto 2 (atualizado) — Painel do Censo Escolar 2024 com Power Query

**Objetivo:** o painel mostra a infraestrutura básica (água, energia, esgoto e lixo), a dependência administrativa, a localização e o porte das escolas de **um município escolhido pelo grupo**, a partir da base completa do Censo Escolar 2024. As tabelas dinâmicas, os gráficos, a segmentação e o dashboard se alimentam de uma tabela tratada pelo Power Query, que filtra o município escolhido.

**O que mudou em relação à versão anterior:** a versão anterior trabalhava com um recorte já pronto das escolas de São Paulo (8.023 escolas), tratado com fórmulas na própria planilha. Agora a planilha importa a **base nacional completa** (todos os municípios do Brasil) via Power Query, e o **filtro é feito dentro do Power Query**, por um Merge com Junção Interna (UF + Município) com a tabela da aba `Filtro`. Assim, as dinâmicas só processam o município escolhido, mesmo com a base tendo centenas de milhares de linhas. As colunas derivadas (Dependência, Localização, Localização Diferenciada, Situação, Tamanho da Escola e os indicadores de Água, Energia, Esgoto e Lixo), antes feitas com PROCV/SE/SES, agora são criadas no Power Query (Merges Esquerda Externa e colunas condicionais).

**Como usar:**
1. Salve o arquivo `Censo_2024_Excel.xlsx` (base nacional do eClass) na pasta **Downloads** e abra `Projeto2_Painel_Censo_PowerQuery.xlsx`.
2. Na aba `Filtro`, informe a **UF** e o **Município**, exatamente como aparecem na base (ex.: SP e São Paulo).
3. Clique em **Dados → Atualizar Tudo** e aguarde o Power Query terminar.
4. Veja o resultado na aba `DINÂMICAS` e no dashboard.
5. As consultas ficam em **Dados → Consultas e Conexões** (`Filtro`, `Dependencia`, `Localizacao`, `LocDiferenciada`, `Situacao`, `BaseBrasil` e `CensoEscolar`). O código está em cada uma, em **Editor Avançado**.

**Estrutura das consultas:** `BaseBrasil` só abre o arquivo do Censo; `CensoEscolar` faz o Merge Interno com `Filtro`, os quatro Merges Esquerda Externa com as tabelas auxiliares e cria as colunas condicionais. Separamos `BaseBrasil` de `CensoEscolar` para evitar o erro de nível de privacidade do Excel, que aparece quando uma mesma consulta abre um arquivo e usa outras consultas.

---

## Uso de Inteligência Artificial

**Ferramenta utilizada:** Claude (Anthropic), no aplicativo web claude.ai.

**Para que foi usada:** (1) sugerir e construir as tabelas dinâmicas de Água, Energia, Esgoto e Lixo da versão anterior; (2) escrever o código M das consultas do Power Query (importação, Merge Interno com o filtro, Merges Esquerda Externa e colunas condicionais), reproduzindo a lógica de prioridade já usada nas fórmulas da planilha; (3) orientar, passo a passo, a montagem e a correção de erros das consultas.

**Exemplo de prompt utilizado:**
> "siga as instruções, me explique e faça tudo o que deve fazer a partir de agora, com esses novos comandos, se der para fazer tudo, faça, o que não der me diga e explique de maneira simples para eu fazer [...]" (acompanhado do roteiro da monitorada de 28/09)

**O que foi ajustado manualmente:** o grupo criou a aba `Filtro` e as quatro tabelas auxiliares na aba `Parâmetros`, colou o código das consultas no Editor Avançado, corrigiu nomes de tabelas e de consultas que causavam erro, separou a consulta `BaseBrasil` da `CensoEscolar` e reapontou as tabelas dinâmicas para a nova tabela tratada.

---

## Fonte de Dados

**Fonte oficial:** Censo Escolar da Educação Básica 2024 (INEP/MEC).

**Link oficial:** https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar

**O que os dados representam:** o Censo Escolar é o principal levantamento estatístico da educação básica brasileira, respondido anualmente por todas as escolas públicas e privadas. Cada linha da base é uma escola, com localização, dependência administrativa, situação de funcionamento, matrículas e infraestrutura.

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

**O que aprendemos com este projeto:** aprendemos que filtrar **antes** de carregar (Merge Interno no Power Query) é o que torna possível trabalhar com uma base nacional de centenas de milhares de linhas sem travar o Excel. Também aprendemos a diferença entre Junção Interna (filtra) e Esquerda Externa (enriquece), a recriar fórmulas de planilha como colunas condicionais do Power Query e a resolver erros de consulta lendo a mensagem do Excel.

**Papel de cada integrante:**
- **João Henrique Viana:** montou a aba `Filtro` (células nomeadas UF e Município) e a consulta principal, com o Merge Interno, e reapontou as tabelas dinâmicas para a nova base.
- **Gustavo Del Gilgio:** importou as tabelas auxiliares (Dependência, Localização, Localização Diferenciada e Situação), fez os Merges Esquerda Externa e conferiu as descrições trazidas.
- **João Vitor Arantes:** criou as colunas condicionais (Tamanho da Escola, Água, Energia, Esgoto e Lixo), conferiu os totais das tabelas dinâmicas e montou o dashboard.
