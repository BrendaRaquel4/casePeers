import os
import pandas as pd
import sys

def carregar_dados():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.normpath(os.path.join(base_dir, "..", "data"))

    arquivos_map = {
        'produtos': 'produtos.csv',
        'clientes': 'clientes.csv',
        'fornecedores': 'fornecedores.csv',
        'estoque': 'estoque.csv',
        'vendas': 'vendas.csv'
    }

    dataframes = {}
    print(" Preparando os dados...")

    for key, nome_arquivo in arquivos_map.items():
        caminho_completo = os.path.join(data_dir, nome_arquivo)
        
        try:
            # Leitura usando TAB
            df = pd.read_csv(
                caminho_completo, 
                sep="\t",
                header=0,
                encoding="utf-8",
                on_bad_lines="skip"
            )

            # Padronizando nomes das colunas
            df.columns = (
                df.columns.str.strip()
                          .str.lower()
                          .str.replace(' ', '_', regex=False)
            )

            dataframes[key] = df

        except FileNotFoundError:
            print(f"ERRO CRÍTICO: Arquivo {caminho_completo} não encontrado.")
            return None
        except Exception as e:
            print(f"ERRO inesperado ao processar o arquivo {nome_arquivo}: {e}", file=sys.stderr)
            return None

    print(" Teste de dados válidos!")
    print(f" Estoque (Chaves): {dataframes['estoque'].columns.tolist()}")
    print(f" Vendas (Chaves): {dataframes['vendas'].columns.tolist()}")
    print(f" Produtos (Chaves): {dataframes['produtos'].columns.tolist()}")
    print(f" Clientes (Chaves): {dataframes['clientes'].columns.tolist()}")

    return dataframes
