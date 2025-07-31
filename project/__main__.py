import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_excel(r'project\database\TESTE.xlsx')
class coleta_dados_materiais:
#isso tudo coleta os dados do excel, os coloca em um dataframe e depois transforma em uma lista de dicionários, que então é transformada em um dataframe novamente 
#para que possa ser utilizado no matplotlib e seaborn posteriormente
    @staticmethod
    def materiais_segunda():
        df = pd.read_excel(r'project\database\TESTE.xlsx')
        segunda_df = df[df['DIA'] == 'segunda']
        # Converte cada linha filtrada em um dicionário
        linhas_completas = segunda_df.to_dict(orient='records')
        # Cria um DataFrame a partir da lista de dicionários
        df_teste = pd.DataFrame(linhas_completas)
        return df_teste


    def materiais_terca():
        df = pd.read_excel(r'project\database\TESTE.xlsx')
        terca_df = df[df['DIA'] == 'terca']
        # Converte cada linha filtrada em um dicionário
        linhas_completas = terca_df.to_dict(orient='records')
        # Cria um DataFrame a partir da lista de dicionários
        df_teste = pd.DataFrame(linhas_completas)
        return df_teste
    
    def materiais_quarta():
        df = pd.read_excel(r'project\database\TESTE.xlsx')
        quarta_df = df[df['DIA'] == 'quarta']
        # Converte cada linha filtrada em um dicionário
        linhas_completas = quarta_df.to_dict(orient='records')
        # Cria um DataFrame a partir da lista de dicionários
        df_teste = pd.DataFrame(linhas_completas)
        return df_teste
    
    def materiais_quinta():
        df = pd.read_excel(r'project\database\TESTE.xlsx')
        materiais_quinta = []
        quinta_df = df[df['DIA'] == 'quinta']
        linhas_completas = quinta_df.to_dict(orient='records')
        # Cria um DataFrame a partir da lista de dicionários
        df_teste = pd.DataFrame(linhas_completas)
        return df_teste
    
    def materiais_sexta():
        df = pd.read_excel(r'project\database\TESTE.xlsx')
        materiais_sexta = []
        sexta_df = df[df['DIA'] == 'sexta']
        # Adiciona os produtos dessas linhas na lista
        linhas_completas = sexta_df.to_dict(orient='records')
        # Cria um DataFrame a partir da lista de dicionários
        df_teste = pd.DataFrame(linhas_completas)
        return df_teste


class media_semanal_materiais:
    @staticmethod
    
    def calculo():
        df = pd.read_excel(r'project\database\TESTE.xlsx')
        # Calcula a média de cada coluna numérica
        media = df.mean(numeric_only=True)
        # Converte a série de médias em um DataFrame
        media_df = pd.DataFrame(media).T
        return media_df

print(media_semanal_materiais.calculo())




