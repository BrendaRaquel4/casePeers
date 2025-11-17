import os
import pandas as pd
from dados.carregarDados import carregar_dados

# Todas as métricas importadas
from metricas.metrica1_vendasCategoria import calcular_vendas_categoria as m1
from metricas.metrica2_margemProduto import calcular_margem_produto as m2
from metricas.metrica3_rankingClientes import calcular_ranking_clientes as m3
from metricas.metrica4_rankingFornecedor import calcular_ranking_estoque_fornecedor as m4
from metricas.metrica5_vendasPorMes import calcular_vendas_por_mes as m5
from metricas.metrica6_estoqueTotalPorFornecedor import calcular_estoque_total_por_fornecedor as m6
from metricas.metrica7_ticketMedioPorCliente import calcular_ticket_medio_por_cliente as m7
from metricas.metrica8_produtosMaisVendidos import calcular_produtos_mais_vendidos as m8
from metricas.metrica9_estoqueCritico import identificar_estoque_critico as m9
from metricas.metrica10_lucroTotalGeral import calcular_lucro_total as m10

def main():
    # 1. Carregando dados
    data = carregar_dados()
    if data is None:
        print("Erro ao carregar dados.")
        return

    # 2. Tratando tipos numéricos
    print("Tratamento e conversão de tipos (Resolvendo R$ 0,00)...")
    data['estoque']['valor_estoque'] = pd.to_numeric(data['estoque']['valor_estoque'], errors='coerce').fillna(0)
    data['estoque']['qtd_estoque'] = pd.to_numeric(data['estoque']['qtd_estoque'], errors='coerce').fillna(0)
    data['vendas']['valor_item'] = pd.to_numeric(data['vendas']['valor_item'], errors='coerce').fillna(0)
    data['vendas']['qtd_item'] = pd.to_numeric(data['vendas']['qtd_item'], errors='coerce').fillna(0)
    print("Tratamento de tipos concluído.\n")

    # 3. Métricas sendo executadas
    print(" Calculando as 10 métricas...")

    # Métrica 1
    m1(data['produtos'], data['vendas'])

    # Métrica 2
    m2(data['produtos'], data['estoque'], data['vendas'])

    # Métrica 3
    m3(data['vendas'], data['clientes'])

    # Métrica 4
    m4(data['estoque'], data['fornecedores'])

    # Métrica 5
    m5(data['vendas'])

    # Métrica 6
    m6(data['estoque'], data['fornecedores'])

    # Métrica 7
    m7(data['vendas'], data['clientes'])

    # Métrica 8
    m8(data['vendas'], data['produtos'])

    # Métrica 9
    m9(data['estoque'])

    # Métrica 10
    m10(data['vendas'], data['produtos'], data['estoque'])

if __name__ == "__main__":
    main()
