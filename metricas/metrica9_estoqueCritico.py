import pandas as pd

def identificar_estoque_critico(estoque):
    critico = estoque[estoque["qtd_estoque"] < 20]
    print("\n Produtos com estoque crítico (menos de 20 unidades):")
    print(critico[["id_estoque", "qtd_estoque"]].head(10))
