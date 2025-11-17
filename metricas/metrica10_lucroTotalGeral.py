import pandas as pd

def calcular_lucro_total(vendas, produtos, custo_unitario_df):
    produtos_custo = produtos.merge(custo_unitario_df, on='id_estoque', how='left')
    vendas_master = vendas.merge(produtos_custo[['id_produto','custo_unitario']], on='id_produto', how='left')

    vendas_master['custo_unitario'] = vendas_master['custo_unitario'].fillna(0)
    vendas_master['cpv'] = vendas_master['qtd_item'] * vendas_master['custo_unitario']

    receita_total = vendas_master['valor_item'].sum()
    custo_total_cpv = vendas_master['cpv'].sum()
    lucro_total = receita_total - custo_total_cpv

    def formatar_valor(valor):
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    print("\n Lucro total estimado (Receita - CPV):")
    print(f"Receita total: {formatar_valor(receita_total)}")
    print(f"Custo dos Produtos Vendidos (CPV): {formatar_valor(custo_total_cpv)}")
    print(f"Lucro estimado (Receita - CPV): {formatar_valor(lucro_total)}")
