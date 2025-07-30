import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_excel(r'project\database\TESTE.xlsx')
def main():
    return 0

class calculo_media_semanal:

    @staticmethod
    def materiais_segunda():
        df = pd.read_excel(r'project\database\TESTE.xlsx')
        materiais_segunda = []
        segunda_df = df[df['DIA'] == 'segunda']
        # Adiciona os produtos dessas linhas na lista
        materiais_segunda = segunda_df['Nome Produtos'].tolist()
        return materiais_segunda

    def materiais_terca():
        df = pd.read_excel(r'project\database\TESTE.xlsx')
        materiais_terca = []
        terca_df = df[df['DIA'] == 'terca']
        # Adiciona os produtos dessas linhas na lista
        materiais_terca = terca_df['Nome Produtos'].tolist()
        return materiais_terca
    
    def materiais_quarta():
        df = pd.read_excel(r'project\database\TESTE.xlsx')
        materiais_quarta = []
        quarta_df = df[df['DIA'] == 'quarta']
        # Adiciona os produtos dessas linhas na lista
        materiais_quarta = quarta_df['Nome Produtos'].tolist()
        return materiais_quarta
    
    def materiais_quinta():
        df = pd.read_excel(r'project\database\TESTE.xlsx')
        materiais_quinta = []
        quinta_df = df[df['DIA'] == 'quinta']
        # Adiciona os produtos dessas linhas na lista
        materiais_quinta = quinta_df['Nome Produtos'].tolist()
        return materiais_quinta
    
    def materiais_sexta():
        df = pd.read_excel(r'project\database\TESTE.xlsx')
        materiais_sexta = []
        sexta_df = df[df['DIA'] == 'sexta']
        # Adiciona os produtos dessas linhas na lista
        materiais_sexta = sexta_df['Nome Produtos'].tolist()
        return materiais_sexta
