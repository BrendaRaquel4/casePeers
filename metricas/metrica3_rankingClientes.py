import pandas as pd

def calcular_ranking_clientes(vendas, clientes):
    # Padroniza colunas (minúsculas e underscores)
    vendas.columns = vendas.columns.str.strip().str.lower().str.replace(' ', '_', regex=False)
    clientes.columns = clientes.columns.str.strip().str.lower().str.replace(' ', '_', regex=False)
    
    # Converte datas corretamente
    vendas['data_nota'] = pd.to_datetime(vendas['data_nota'], errors='coerce')
    
    # Cria coluna mês/ano
    vendas['mes_ano'] = vendas['data_nota'].dt.to_period('M').astype(str)
    
    # Combina vendas com clientes
    df_combinado = vendas.merge(
        clientes[['id_cliente', 'nome_cliente']],
        on='id_cliente',
        how='left'
    )
    
    # Juntando cliente e mês, somando quantidade de itens
    ranking = df_combinado.groupby(['nome_cliente', 'mes_ano'])['qtd_item'].sum().reset_index()
    
    # Ordena por mês e quantidade (maior para menor)
    ranking = ranking.sort_values(['mes_ano', 'qtd_item'], ascending=[True, False])
    
    # Top 5 clientes por mês
    top_clientes_por_mes = ranking.groupby('mes_ano').head(5).reset_index(drop=True)
    
    # Exibindo resultados
    print("\n Ranking de Clientes por Quantidade Comprada por Mês (Top 5):")
    for mes in top_clientes_por_mes['mes_ano'].unique():
        print(f"\nMês: {mes}")
        print(
            top_clientes_por_mes[top_clientes_por_mes['mes_ano'] == mes]
            .rename(columns={'qtd_item': 'qtd_total_comprada'})
            .drop(columns=['mes_ano'])
        )
