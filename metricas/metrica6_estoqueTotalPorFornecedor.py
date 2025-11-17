import pandas as pd

def calcular_estoque_total_por_fornecedor(estoque, fornecedores):
    estoque_copy = estoque.copy()
    estoque_copy["valor_estoque_num"] = pd.to_numeric(estoque_copy["valor_estoque"], errors='coerce')
    
    # Juntando fornecedor
    total = estoque_copy.groupby("id_fornecedor", as_index=False)["valor_estoque_num"].sum()
    total = total.merge(fornecedores, on="id_fornecedor")

    # Exibindo top 10
    print("\n Valor total de estoque por fornecedor (Top 10):")
    print(
        total[["nome_fornecedor", "valor_estoque_num"]]
        .rename(columns={"valor_estoque_num": "VALOR TOTAL ESTOQUE (R$)"})
        .sort_values("VALOR TOTAL ESTOQUE (R$)", ascending=False)
        .head(10)
    )
    
    return total
