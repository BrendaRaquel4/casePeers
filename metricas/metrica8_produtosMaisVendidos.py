import pandas as pd

def calcular_produtos_mais_vendidos(vendas, produtos):
    ranking = vendas.groupby("id_produto", as_index=False)["qtd_item"].sum()
    ranking = ranking.merge(produtos, on="id_produto", how="left")
    ranking = ranking.sort_values("qtd_item", ascending=False).head(10)

    print("\n Top 10 produtos mais vendidos:")
    print(ranking[["nome_produto", "categoria", "qtd_item"]])
