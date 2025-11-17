import pandas as pd

def calcular_ranking_estoque_fornecedor(estoque, fornecedores):
    estoque['data_estoque'] = pd.to_datetime(estoque['data_estoque'])
    estoque['mes_ano'] = estoque['data_estoque'].dt.to_period('M').astype(str)

    # Combinando fornecedores
    df_combinado = estoque.merge(fornecedores, on='id_fornecedor', how='left')

    # Juntando fornecedor e mês, somando quantidade de estoque
    ranking_estoque = df_combinado.groupby(['nome_fornecedor', 'mes_ano'])['qtd_estoque'].sum().reset_index()

    # Ordena por mês e quantidade
    ranking_estoque = ranking_estoque.sort_values(['mes_ano', 'qtd_estoque'], ascending=[True, False])

    print("\n Ranking de Fornecedores por Estoque (Top 10 Geral):")
    print(
        ranking_estoque.rename(columns={'qtd_estoque': 'QTD Total Estoque'}).head(10)
    )
