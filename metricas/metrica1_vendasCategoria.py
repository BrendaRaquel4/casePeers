import pandas as pd

def calcular_vendas_categoria(produtos, vendas):
    # 1. Mescla Vendas com Produtos para obter a Categoria
    vendas_merged = vendas.merge(produtos, on="id_produto", how="left")

    # 2. Calcula o valor total de cada item (valor_item * qtd_item)
    vendas_merged["valor_total"] = vendas_merged["valor_item"] * vendas_merged["qtd_item"]

    # 3. Agrupa por categoria e soma o valor_total
    resultado = (
        vendas_merged.groupby("categoria", as_index=False)["valor_total"]
        .sum()
        .sort_values("valor_total", ascending=False)
    )

    print("\nValor total de venda por categoria:")
    print(resultado)
