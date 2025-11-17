import pandas as pd

def calcular_ticket_medio_por_cliente(vendas, clientes):
    ticket = vendas.groupby("id_cliente", as_index=False)["valor_nota"].mean()
    ticket = ticket.merge(clientes, on="id_cliente", how="left")
    
    print("\n Ticket médio por cliente (Top 10):")
    print(ticket[["nome_cliente", "valor_nota"]].head(10))
