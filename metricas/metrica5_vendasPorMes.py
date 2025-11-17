import pandas as pd

def calcular_vendas_por_mes(vendas):
    vendas["data_nota"] = pd.to_datetime(vendas["data_nota"], errors="coerce")
    vendas["mes_ano"] = vendas["data_nota"].dt.to_period("M").astype(str)

    vendas_por_mes = (
        vendas.groupby("mes_ano")["valor_item"]
        .sum()
        .reset_index()
        .rename(columns={"valor_item": "total_vendas"})
    )

    print("\n Vendas Totais por Mês:")
    print(vendas_por_mes)
