import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime as dt

try:
    df = pd.read_excel(r'project\database\NOVO INVENTARIO UNIFICADO 3.0.xlsx')
except FileNotFoundError:
    print("Certifique-se de que o 'arquivo.xlsx' está no mesmo diretório do seu script, ou forneça o caminho completo.")
    exit()
class coleta_dados_materiais:
#isso tudo coleta os dados do excel, os coloca em um dataframe e depois transforma em uma lista de dicionários, que então é transformada em um dataframe novamente 
#para que possa ser utilizado no matplotlib e seaborn posteriormente
    @staticmethod
    def materiais_segunda():
        df = pd.read_excel(r'project\database\NOVO INVENTARIO UNIFICADO 3.0.xlsx', header=None)
        primeira_linha = df.iloc[0]
    
    # Procura o índice da coluna que contém "DIA"
        idx_dia = None
        for i, valor in enumerate(primeira_linha):
            if str(valor).strip().lower() == "dia":
                idx_dia = i
                break
    
        if idx_dia is None:
            print("Coluna 'DIA' não encontrada.")
            return None
    # Define os nomes das colunas usando a primeira linha
        df.columns = primeira_linha
    # Remove a primeira linha do DataFrame (pois agora é o cabeçalho)
        df = df[1:]
    # Filtra as linhas onde a coluna 'DIA' contém 'SEGUNDA-FEIRA'
        colunas_desejadas = [col for col in df.columns if str(col).strip().lower() in ["dia", "nome produto"]]
        dados_segunda = df[df['DIA'].str.contains('SEGUNDA-FEIRA', case=False, na=False)][colunas_desejadas]
        return dados_segunda


    
class media_semanal_materiais:
    @staticmethod
    
    def calculo():
        df = pd.read_excel(r'project\database\TESTE.xlsx')
        segunda_feira_columns = [col for col in df.columns if 'segunda-feira' in col.lower()]
        segunda_feira_data = df[segunda_feira_columns] 
        print("\nData from 'segunda-feira' columns:")
        print(segunda_feira_data)

print(coleta_dados_materiais.materiais_segunda())




