 Candidata: Brenda Raquel Maia Gonçalves
 
 A solução utiliza Python e Pandas para tratar, estruturar e analisar dados de 5 tabelas fornecidas pelo cliente.

Tecnologias Utilizadas:
    1. Python 3
    2. Pandas
    3. VS Code

O case é composto por cinco tabelas:

 1. Cadastro de Produtos

        ID_PRODUTO
        ID_ESTOQUE
        NOME_PRODUTO
        CATEGORIA

2. Cadastro de Clientes

        ID_CLIENTE
        NOME_CLIENTE
        DATA_CADASTRO

3. Transações / Notas de Venda
        ID_NOTA
        DATA_NOTA
        VALOR_NOTA
        VALOR_ITEM
        QTD_ITEM
        ID_PRODUTO
        ID_CLIENTE

4. Cadastro de Estoque
        ID_ESTOQUE
        VALOR_ESTOQUE
        QTD_ESTOQUE
        DATA_ESTOQUE
        ID_FORNECEDOR

5. Cadastro de Fornecedores
        ID_FORNECEDOR
        NOME_FORNECEDOR
        DATA_CADASTRO

Carregamento dos Dados: Os arquivos CSV devem estar na mesma pasta do projeto com os nomes:
    produtos.csv
    clientes.csv
    transacoes.csv
    estoque.csv
    fornecedores.csv

Análises observadas:
Rentabilidade por Produto e Categoria
    Combinação de produtos + transações para calcular:
        1. Receita total
        2. Quantidade vendida
        3. Ticket médio
        4. Rentabilidade por categoria

    Vendas por Cliente
        1. Ranking dos clientes por valor total comprado

    Valor total de estoque por fornecedor
        1. Cálculo implementado no código


Como executar o projeto:

1. Abra a pasta do projeto no VS Code 

2. Tenha Python instalado

3. Instale as dependências: pip install pandas

4. Execute: python main.py
