import pandas as pd

def calcular_margem_produto(produtos, estoque, vendas):
    # 1. Calcular custo unitário médio por estoque
    estoque['custo_unitario'] = estoque['valor_estoque'] / estoque['qtd_estoque']

    # 2. Juntar vendas com produtos
    df_vendas_produtos = vendas.merge(
        produtos[['id_produto', 'id_estoque', 'nome_produto', 'categoria']],
        on='id_produto',
        how='left'
    )

    # 3. Juntar com o estoque para pegar custo unitário
    df_margem = df_vendas_produtos.merge(
        estoque[['id_estoque', 'custo_unitario']],
        on='id_estoque',
        how='left'
    )

    # 4. Calcular margem por item
    df_margem['custo_unitario'] = df_margem['custo_unitario'].fillna(0)
    df_margem['margem_item'] = df_margem['valor_item'] - df_margem['custo_unitario']

    # 5. Ranking por produto
    ranking_margem = df_margem.groupby(
        ['nome_produto', 'categoria']
    )['margem_item'].sum().reset_index()

    ranking_margem = ranking_margem.sort_values(
        'margem_item', ascending=False
    ).head(10)

    print("\n Ranking de Margem Total por Produto (Top 10):")
    print(ranking_margem.rename(columns={'margem_item': 'MARGEM_TOTAL(R$)'}))
