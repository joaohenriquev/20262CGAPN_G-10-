# Projeto 1 (atualizado) — Simulador de Repasse do PNAE com Automação em VBA

**Objetivo:** o simulador calcula o repasse anual estimado do PNAE para uma escola a partir das matrículas por modalidade e permite simular cenários com um Fator de Ajuste. Nesta versão, uma macro em VBA grava cada simulação (data/hora, fator, racional, resultado e usuário) em uma aba de banco de dados, para que qualquer pessoa que reabra a planilha entenda **por que** aquele fator foi escolhido, e não só qual foi o resultado numérico.

**Como usar:**
1. Abra `Simulador-PNAE-Projeto1.xlsm` e habilite as macros.
2. Na aba `Simulador_Escola`, preencha o **Fator de Ajuste** (C26), o **Racional da Taxa** (C25, texto livre explicando o motivo) e o **Usuário** (F25, seu nome).
3. Clique no botão **Registrar simulação**. A macro `RegistrarSimulacao` valida os campos, grava uma linha na aba `Banco_de_Dados` e limpa os três campos para a próxima simulação.
4. Consulte o histórico na aba `Banco_de_Dados` (ID, Data/Hora, Fator de Ajuste, Racional da Taxa, Total de Matrículas Ajustadas, Repasse Ajustado, Usuário).

**O que mudou em relação à versão anterior:** campo *Racional da Taxa* (C25), campo *Usuário* (F25), aba `Banco_de_Dados`, botão e módulo VBA `modSimulador` (`RegistrarSimulacao`, `ValidarSimulacao`, `LimparCampos`). Atenção: a macro usa endereços fixos (C25, C26, F25, C35, D35); inserir linhas/colunas acima deles quebra o código.

---

## Uso de Inteligência Artificial

**Ferramenta utilizada:** Claude (Anthropic), no aplicativo web claude.ai.

**Para que foi usada:** (1) gerar o artefato HTML interativo do simulador (versão anterior do projeto); (2) escrever o módulo VBA desta versão, implementando os quatro passos do campo Usuário (criar, ler, validar, gravar/limpar) e o desafio extra de aviso para fatores fora de −50% a +50%; (3) preparar o layout da planilha (campos C25 e F25 e a aba `Banco_de_Dados`).

**Exemplo de prompt utilizado:**
> "siga as instruções, me explique e faça tudo o que deve fazer a partir de agora, com esses novos comandos, se der para fazer tudo, faça, o que não der me diga e explique de maneira simples para eu fazer, [...] apenas siga este documento, use tudo que já fizemos." (acompanhado do roteiro das atividades monitoradas de 24/09 e 28/09)

**O que foi ajustado manualmente:** o grupo criou o botão na planilha e o associou à macro, colou o módulo no editor do VBA, salvou o arquivo como Pasta de Trabalho Habilitada para Macro (.xlsm) e testou o funcionamento no Excel (veja a seção de participação).

---

## Fonte de Dados

**Fonte oficial:** Resolução CD/FNDE nº 1, de 18 de fevereiro de 2026 (que altera a Resolução CD/FNDE nº 6/2020), com valores per capita consolidados em 2026.

**Link oficial:** https://www.gov.br/fnde/pt-br/acesso-a-informacao/acoes-e-programas/programas/pnae

**O que os dados representam:** valores per capita diários (R$/dia por aluno) do PNAE por modalidade de ensino e os 200 dias letivos usados no cálculo anual. Escola (EMEB Vila Quitaúna, Osasco/SP) e matrículas são fictícias, criadas para fins didáticos.

**Estrutura:** aba `Parametros_PNAE` (modalidade, valor per capita, dias letivos, faixas de porte); aba `Simulador_Escola` (matrículas, total, porte, repasse, elegibilidade, fator de ajuste, Tabela de Dados); aba `Banco_de_Dados` (histórico das simulações: ID, Data/Hora, Fator de Ajuste, Racional da Taxa, Total de Matrículas Ajustadas, Repasse Ajustado, Usuário).

---

## Participação do Grupo

**O que aprendemos com este projeto:** aprendemos a transformar uma planilha de cálculo em uma ferramenta com memória: usar uma macro para ler células, validar entradas, gravar em um banco de dados e limpar a tela. Também aprendemos que o código VBA depende de endereços fixos de células e que mudanças de layout podem quebrá-lo, e que registrar o *racional* de uma decisão é tão importante quanto registrar o número.

**Papel de cada integrante:**
- **João Henrique Viana:** criou o campo **Usuário** na tela do simulador (célula F25, ao lado do Racional da Taxa), posicionou o botão e salvou o arquivo como .xlsm.
- **Gustavo Del Gilgio:** implementou o campo Usuário no código VBA: declarou a variável `usuario` e fez a leitura em `RegistrarSimulacao`, a validação em `ValidarSimulacao` (mensagem de erro e bloqueio quando em branco), a gravação na coluna G do `Banco_de_Dados` e a limpeza em `LimparCampos`.
- **João Vitor Arantes:** testou a automação com três simulações diferentes (ex.: −5% com racional "queda de nascimentos pelo Censo"; +10%; 0%), uma tentativa com o Usuário em branco (a validação bloqueou o registro, como esperado) e uma com fator de −60% (o aviso de faixa usual apareceu), e conferiu que os campos foram limpos após cada registro.
