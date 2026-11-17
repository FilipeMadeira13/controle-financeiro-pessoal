# BACKLOG — Controle financeiro pessoal

## 1. Visão geral

**Objetivo:** controlar suas despesas, estimar quanto sobra para investir e comparar cenários hipotéticos de investimento.

**Público:** somente você, com acesso privado pelo navegador do celular e do computador.

**MVP — primeira versão utilizável:**

- Registrar receitas e despesas manualmente, com categorias e consulta mensal.
- Controlar cartões, faturas e compras parceladas.
- Calcular a sobra mensal após compromissos e margem de segurança.
- Comparar dois cenários hipotéticos de investimento.
- Disponibilizar o site pela internet, com login e cópias de segurança.

**Stack:** Python 3.13, Django 5.2 LTS, templates HTML, CSS, JavaScript apenas quando necessário e SQLite. Usar os testes integrados do Django. Essas versões de Python e Django são compatíveis. ([Documentação](https://docs.djangoproject.com/en/5.2/faq/install/))

**Hospedagem:** PythonAnywhere gratuito, com renovação mensal manual. SQLite está disponível no serviço. Conferir novamente os limites antes de publicar. ([Plano gratuito](https://help.pythonanywhere.com/pages/FreeAccountsFeatures/), [bancos disponíveis](https://help.pythonanywhere.com/pages/KindsOfDatabases))

**Fora do MVP:** integração bancária, importação de extratos, saldos por conta bancária, cadastro público, cotações automáticas, impostos, recomendações de produtos e pagamentos parciais de faturas.

**Disponibilidade:** 5–8 horas semanais, sem prazo fixo. Estimativa inicial de aproximadamente 90–100 horas, além de estudo e eventuais ajustes.

**Arquivo:** `BACKLOG.md`.

## 2. Regras e forma de trabalho

### Decisões de funcionamento

- Usar português brasileiro, reais e fuso `America/Fortaleza`.
- Armazenar valores financeiros em centavos inteiros; usar `Decimal` nos cálculos do simulador.
- Considerar receitas e despesas no mês da data prevista informada. Marcar como recebido ou pago não altera o total previsto.
- Considerar despesas do cartão no mês da respectiva fatura. O pagamento da fatura não gera uma segunda despesa.
- Escolher manualmente o mês da primeira fatura de uma compra.
- Distribuir parcelas pelos meses seguintes, preservando o valor total. Ajustar diferenças de centavos na última parcela e permitir conferência antes de salvar.
- Impedir alteração ou exclusão de compras vinculadas a alguma fatura paga. Permitir desfazer a marcação de pagamento antes de corrigir os dados.
- Calcular: **resultado mensal = receitas − despesas fora do cartão − parcelas das faturas**.
- Calcular: **disponível estimado = máximo entre zero e resultado mensal − margem de segurança**. Mostrar separadamente eventual déficit.
- Usar margem zero até você definir outro valor para o mês.
- No simulador, compartilhar valor inicial, contribuição mensal e prazo entre dois cenários; informar uma taxa anual efetiva para cada um.
- Converter a taxa anual em equivalente mensal, aplicar juros compostos e considerar contribuições no final de cada mês.
- Apresentar resultados brutos e identificar as taxas como hipóteses. O simulador não executa investimentos.

### Como executar o backlog

Cada item contém **ID, estimativa, dependências e critério de conclusão**. As estimativas são aproximadas; nenhuma tarefa deve ultrapassar duas horas sem ser novamente dividida.

Você escreverá os testes e a implementação. Nas regras financeiras, seguir **RED → GREEN → REFACTOR**: demonstrar uma falha, implementar o necessário e melhorar a organização mantendo os testes.

Antes de instalações, gravações, mudanças no Git ou operações externas, explicar o impacto e obter sua aprovação. Ao concluir uma tarefa, apresentar evidências e aguardar sua decisão antes de avançar.

## 3. Microtarefas em ordem de execução

### Fase 1 — Acesso privado funcionando localmente

**Entrega testável:** abrir o site, entrar com sua conta e acessar uma página privada.

- [x] Verificar o estado do Git e preparar uma branch de trabalho mediante aprovação (**A01**, 1h; dependências: nenhuma). **Pronto:** contexto registrado e trabalho preparado fora de `main/master`.
- [x] Preparar o ambiente Python e registrar dependências e arquivos ignorados pelo Git (**A02**, 1h; depende de A01). **Pronto:** ambiente reproduzível; segredos, bancos e backups excluídos do versionamento.
- [x] Criar o projeto Django com SQLite e configurações por ambiente (**A03**, 1h; depende de A02). **Pronto:** servidor local inicia e a verificação do Django executa sem erros.
- [x] Construir uma página base adaptada ao celular e computador (**A04**, 2h; depende de A03). **Pronto:** navegação e conteúdo permanecem utilizáveis nos dois tamanhos.
- [ ] Escrever testes de login, credenciais inválidas e acesso anônimo (**A05**, 1h; depende de A03). **Pronto:** os testes demonstram a ausência do comportamento esperado.
- [ ] Implementar login, logout e proteção das páginas privadas (**A06**, 2h; depende de A04 e A05). **Pronto:** sua conta acessa a página privada e os testes passam.
- [ ] Demonstrar o fluxo completo de acesso e registrar o aprendizado (**A07**, 1h; depende de A06). **Pronto:** entrar, sair e reiniciar a aplicação funciona; você explica como uma página é protegida.

### Fase 2 — Receitas e despesas organizadas por mês

**Entrega testável:** registrar movimentações e consultar totais mensais por categoria.

- [ ] Escrever testes das regras básicas de movimentação (**B01**, 1h; depende de A07). **Pronto:** cobrir valor positivo, data, categoria e distinção entre receita e despesa.
- [ ] Implementar o armazenamento das movimentações e suas migrações (**B02**, 2h; depende de B01). **Pronto:** os registros persistem e os testes passam.
- [ ] Criar o cadastro e a listagem de categorias (**B03**, 2h; depende de B02). **Pronto:** cadastrar uma categoria e utilizá-la em um lançamento funciona.
- [ ] Criar o formulário de receitas (**B04**, 1h; depende de B03). **Pronto:** registrar descrição, valor, data, categoria e situação de recebimento funciona.
- [ ] Criar o formulário de despesas fora do cartão (**B05**, 1h; depende de B03). **Pronto:** registrar uma despesa paga ou pendente funciona.
- [ ] Implementar edição e exclusão confirmada de movimentações (**B06**, 2h; depende de B04 e B05). **Pronto:** corrigir ou remover um registro atualiza os dados exibidos.
- [ ] Construir a listagem com filtro de mês e ano (**B07**, 2h; depende de B06). **Pronto:** cada mês mostra somente seus lançamentos; meses vazios têm uma mensagem clara.
- [ ] Escrever testes dos totais mensais e por categoria (**B08**, 1h; depende de B07). **Pronto:** cobrir virada do ano, mês vazio e registros pagos ou pendentes sem duplicação.
- [ ] Implementar o resumo mensal de receitas e despesas (**B09**, 2h; depende de B08). **Pronto:** totais gerais e por categoria correspondem aos valores esperados.
- [ ] Conferir um mês fictício pelo celular e explicar os totais (**B10**, 1h; depende de B09). **Pronto:** cadastro, correção, exclusão e consulta produzem resultados conferidos manualmente.

### Fase 3 — Cartões e faturas com compras à vista

**Entrega testável:** cadastrar cartões, registrar compras e acompanhar o pagamento integral das faturas.

- [ ] Criar o cadastro e a listagem de cartões (**C01**, 2h; depende de B10). **Pronto:** cadastrar nome e dia de vencimento sem armazenar número ou código de segurança.
- [ ] Implementar faturas identificadas por cartão e mês (**C02**, 2h; depende de C01). **Pronto:** não existem faturas duplicadas; vencimentos em dias inexistentes usam o último dia do mês.
- [ ] Escrever testes de compra vinculada à fatura escolhida (**C03**, 1h; depende de C02). **Pronto:** cobrir cartão, categoria, valor e mês de referência.
- [ ] Implementar o registro de compras de uma parcela (**C04**, 2h; depende de C03). **Pronto:** a compra aparece na fatura selecionada e os testes passam.
- [ ] Construir a consulta de itens e total de cada fatura (**C05**, 1h; depende de C04). **Pronto:** dois cartões no mesmo mês mantêm faturas e totais separados.
- [ ] Escrever testes de pagamento integral e contagem de despesas (**C06**, 1h; depende de C05). **Pronto:** marcar uma fatura como paga não cria outra despesa.
- [ ] Implementar a marcação e o desfazimento do pagamento integral (**C07**, 2h; depende de C06). **Pronto:** situação e data de pagamento são atualizadas corretamente.
- [ ] Integrar compras do cartão ao resumo mensal e por categoria (**C08**, 2h; depende de C07 e B09). **Pronto:** os gastos aparecem uma única vez, no mês da fatura.
- [ ] Implementar correção e exclusão de compras em faturas pendentes (**C09**, 2h; depende de C08). **Pronto:** os totais são recalculados e compras de faturas pagas ficam protegidas.
- [ ] Conferir um cenário com dois cartões e faturas pagas e pendentes (**C10**, 1h; depende de C09). **Pronto:** os totais coincidem com uma conferência manual.

### Fase 4 — Compras parceladas

**Entrega testável:** registrar uma compra parcelada e consultar seus compromissos futuros.

- [ ] Escrever testes de divisão em parcelas e avanço dos meses (**D01**, 1h; depende de C10). **Pronto:** cobrir divisão com centavos, parcela única e passagem de dezembro para janeiro.
- [ ] Implementar a distribuição dos valores e meses das parcelas (**D02**, 2h; depende de D01). **Pronto:** a soma das parcelas preserva exatamente o valor da compra.
- [ ] Adicionar quantidade de parcelas e prévia ao formulário de compra (**D03**, 2h; depende de D02). **Pronto:** visualizar valores e faturas antes de confirmar funciona.
- [ ] Permitir conferir e ajustar os valores da prévia (**D04**, 1h; depende de D03). **Pronto:** somente parcelas positivas cuja soma corresponda ao total podem ser confirmadas.
- [ ] Salvar a compra e suas parcelas em uma única operação (**D05**, 2h; depende de D04). **Pronto:** uma falha não deixa uma compra parcialmente registrada.
- [ ] Adaptar a correção e exclusão de compras parceladas (**D06**, 2h; depende de D05 e C09). **Pronto:** alterações não duplicam parcelas e respeitam a proteção de faturas pagas.
- [ ] Exibir as parcelas nas consultas dos meses futuros (**D07**, 1h; depende de D05). **Pronto:** cada parcela aparece na fatura e no resumo do mês correspondente.
- [ ] Conferir parcelamentos novos e já iniciados em meses anteriores (**D08**, 1h; depende de D06 e D07). **Pronto:** valores, meses e quantidade de parcelas correspondem ao cenário registrado.

### Fase 5 — Sobra mensal e margem de segurança

**Entrega testável:** consultar o valor disponível estimado para investir em determinado mês.

- [ ] Criar a configuração de margem de segurança por mês (**E01**, 1h; depende de D08). **Pronto:** informar ou alterar a margem funciona; o padrão é zero.
- [ ] Escrever testes do cálculo de disponibilidade (**E02**, 1h; depende de E01). **Pronto:** cobrir mês vazio, sobra positiva, déficit e margem superior à sobra.
- [ ] Implementar o cálculo mensal incluindo as parcelas das faturas (**E03**, 1h; depende de E02). **Pronto:** os resultados coincidem com os exemplos dos testes.
- [ ] Exibir resultado mensal, margem e disponível estimado no painel (**E04**, 2h; depende de E03). **Pronto:** eventual déficit aparece claramente e a estimativa identifica o mês e os registros considerados.
- [ ] Conferir o cálculo antes e depois do pagamento de uma fatura (**E05**, 1h; depende de E04). **Pronto:** pagar a fatura não desconta seu valor novamente; alterar a margem atualiza a disponibilidade.

### Fase 6 — Comparação de cenários de investimento

**Entrega testável:** comparar dois cenários hipotéticos com as mesmas contribuições e prazo.

- [ ] Documentar entradas, unidades e fórmula do simulador (**F01**, 1h; depende de E05). **Pronto:** definir taxa anual efetiva, prazo em meses e contribuições no final do mês.
- [ ] Escrever testes com resultados conhecidos (**F02**, 1h; depende de F01). **Pronto:** cobrir taxa zero, contribuições mensais e taxas anuais positivas e negativas.
- [ ] Implementar o cálculo com precisão decimal (**F03**, 2h; depende de F02). **Pronto:** os testes passam e o arredondamento monetário ocorre na apresentação dos resultados.
- [ ] Construir o formulário de dois cenários (**F04**, 2h; depende de F03). **Pronto:** informar valor inicial, contribuição, prazo, identificação e taxa de cada cenário funciona.
- [ ] Exibir a comparação de resultados brutos (**F05**, 1h; depende de F04). **Pronto:** mostrar total contribuído, valor final e rendimento ou perda, com as hipóteses utilizadas.
- [ ] Permitir preencher a contribuição com a sobra mensal estimada (**F06**, 1h; depende de F05 e E04). **Pronto:** o valor sugerido vem do mês selecionado e continua editável.
- [ ] Validar entradas inválidas e apresentar mensagens claras (**F07**, 1h; depende de F06). **Pronto:** rejeitar valores monetários negativos, prazo não positivo e taxa anual igual ou inferior a −100%.
- [ ] Conferir o simulador pelo celular com cálculos independentes (**F08**, 1h; depende de F07). **Pronto:** validar pelo menos um cenário sem rendimento e outro com rendimento; explicar contribuição e rendimento separadamente.

### Fase 7 — Publicação e manutenção básica

**Entrega testável:** acessar o sistema privado pela internet, com dados persistentes e recuperação demonstrada.

- [ ] Criar um procedimento de cópia consistente do SQLite (**G01**, 1h; depende de F08). **Pronto:** gerar uma cópia em local privado, fora dos arquivos públicos e do Git.
- [ ] Restaurar uma cópia em ambiente local separado (**G02**, 1h; depende de G01). **Pronto:** recuperar os registros sem sobrescrever o banco original.
- [ ] Preparar as configurações de publicação (**G03**, 1h; depende de G02). **Pronto:** configurar segredo externo ao código, domínio permitido, depuração desativada e proteção de sessão em HTTPS.
- [ ] Executar a suíte e as verificações de publicação do Django (**G04**, 1h; depende de G03). **Pronto:** registrar resultados, tratar problemas aplicáveis e verificar proteção das páginas financeiras.
- [ ] Revalidar o plano gratuito e preparar a conta com aprovação (**G05**, 1h; depende de G04). **Pronto:** confirmar limites, versão de Python e renovação, sem contratar recursos pagos.
- [ ] Enviar o código e preparar o ambiente na hospedagem (**G06**, 2h; depende de G05). **Pronto:** instalar as dependências registradas, sem enviar dados reais ou segredos pelo Git.
- [ ] Configurar a aplicação Django e os arquivos estáticos (**G07**, 1h; depende de G06). **Pronto:** páginas e estilos carregam; banco e backups ficam fora das rotas públicas.
- [ ] Preparar o banco e a conta privada mediante aprovação de publicação (**G08**, 1h; depende de G07). **Pronto:** aplicar migrações autorizadas e acessar o site com sua conta.
- [ ] Verificar o funcionamento publicado pelo celular (**G09**, 1h; depende de G08). **Pronto:** cadastrar um registro fictício, reiniciar a aplicação e confirmar sua persistência.
- [ ] Documentar renovação, backup, recuperação de acesso e atualização (**G10**, 1h; depende de G09). **Pronto:** conseguir seguir o procedimento; prever backup semanal e antes de atualizações.

### Fase 8 — Conferência de um mês real

**Entrega testável:** utilizar um mês real para validar o MVP completo.

- [ ] Escolher um mês encerrado e reunir os registros necessários (**H01**, 1h; depende de G10). **Pronto:** separar receitas, despesas e faturas sem adicioná-las ao repositório.
- [ ] Registrar as movimentações da primeira semana (**H02**, 2h; depende de H01). **Pronto:** incluir receitas, despesas e compras correspondentes, verificando possíveis duplicações.
- [ ] Registrar as movimentações da segunda semana (**H03**, 2h; depende de H02). **Pronto:** conferir os lançamentos com os documentos de origem.
- [ ] Registrar as movimentações da terceira semana (**H04**, 2h; depende de H03). **Pronto:** conferir os lançamentos com os documentos de origem.
- [ ] Registrar as movimentações restantes do mês (**H05**, 2h; depende de H04). **Pronto:** completar o período, incluindo compras parceladas de meses anteriores presentes nas faturas.
- [ ] Comparar cada fatura do sistema com sua fatura real (**H06**, 1h; depende de H05). **Pronto:** explicar e corrigir todas as diferenças encontradas.
- [ ] Conferir receitas, despesas, margem e disponibilidade manualmente (**H07**, 1h; depende de H06). **Pronto:** os valores do painel coincidem com a conferência independente.
- [ ] Executar duas simulações pelo celular e realizar um backup (**H08**, 1h; depende de H07). **Pronto:** concluir os fluxos sem impedimentos e confirmar a existência da cópia.
- [ ] Revisar o aprendizado e registrar melhorias observadas (**H09**, 1h; depende de H08). **Pronto:** explicar por que pagar a fatura não gera outra despesa e por que a taxa simulada é uma hipótese.

Se algum lote de dados reais exigir mais de duas horas, dividi-lo em lotes menores antes de começar.

## 4. Critérios de conclusão do MVP

O MVP estará concluído quando:

- O acesso pela internet funcionar no celular e no computador, com páginas financeiras protegidas.
- Um mês real estiver registrado e seus totais e faturas estiverem conferidos.
- Parcelas futuras e margem de segurança participarem corretamente da estimativa mensal.
- O simulador apresentar resultados coerentes com os cálculos de referência.
- Os testes e verificações previstos tiverem resultados registrados, com problemas impeditivos resolvidos.
- Uma cópia de segurança tiver sido restaurada com sucesso em ambiente separado.
- Você conseguir realizar os fluxos principais e explicar as regras financeiras implementadas.

## 5. Evoluções desejáveis

Estas ideias ficam fora da estimativa do MVP e precisam de uma nova definição antes de virar microtarefas:

1. **Metas financeiras:** definir objetivos e acompanhar quanto falta acumular.
2. **Carteira de investimentos:** registrar investimentos e acompanhar sua evolução.
3. **Movimentações recorrentes:** gerar receitas e despesas periódicas automaticamente.

**Primeira tarefa de desenvolvimento:** A01. Executar somente após revisar seu impacto e obter sua aprovação.
