# Casos de Teste para Ecommerce

| ID | Nome do Caso | Pré-condição | Passos | Dados de Entrada | Resultado Esperado | Observações |
|---|---|---|---|---|---|---|
| 1 | Inserir produto | Conexão ao banco de dados de produtos ativa; tabela `produtos` criada e vazia | 1. Inserir produto com nome e preço válidos 2. Consultar a tabela `produtos` 3. Verificar dados retornados | nome = "Caneca", preco = 29.90 | Produto é inserido com `id`, `nome` e `preco` corretos | O teste valida criação e leitura de produto na tabela |
| 2 | Banco de produtos vazio | Conexão ao banco de dados de produtos ativa; tabela `produtos` criada e vazia | 1. Consultar a tabela `produtos` 2. Verificar que nenhum registro é retornado | nenhum | Consulta retorna lista vazia | Garante que a fixture de função cria banco limpo para cada teste |
| 3 | Registrar log | Conexão ao banco de dados de logs ativa; tabela `auditoria` criada e vazia | 1. Inserir evento de log 2. Consultar a tabela `auditoria` 3. Verificar dados retornados | evento = "usuario_logado" | Evento é inserido com `id` e `evento` corretos | Validação de auditoria na fixture de sessão |
| 4 | Logs compartilhados | Conexão ao banco de dados de logs ativa; tabela `auditoria` criada e vazia no início da sessão | 1. Inserir primeiro evento 2. Inserir segundo evento 3. Consultar a tabela `auditoria` 4. Verificar quantidade de registros | evento1 = "usuario_logado", evento2 = "pagamento_realizado" | Dois eventos são persistidos e visíveis na mesma sessão | Confirma que a fixture `db_logs` compartilha o mesmo banco entre testes |

## Observações

- A fixture `db_produtos` será criada com escopo padrão de função.
- A fixture `db_logs` será criada com escopo de sessão para compartilhar o mesmo banco de auditoria entre testes.
