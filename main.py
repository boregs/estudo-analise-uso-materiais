import pandas as pd

databases = ['SEGUNDAS','TERCAS','QUARTAS','QUINTAS','SEXTAS']
df = pd.read_excel(r"database\DATABASE_ATUALIZADA.xlsx", sheet_name=databases)
df_segunda = df['SEGUNDAS']

# limpando planilha de segunda

df_segunda = df['SEGUNDAS']
df_segunda = df_segunda.drop_duplicates()

# itens null nao estavam na contagem
df_segunda["segunda-feira, 5 de maio de 2025"] = df_segunda['segunda-feira, 5 de maio de 2025'].fillna(0)
df_segunda["segunda-feira, 12 de maio de 2025"] = df_segunda['segunda-feira, 12 de maio de 2025'].fillna(0)
df_segunda["segunda-feira, 19 de maio de 2025"] = df_segunda['segunda-feira, 19 de maio de 2025'].fillna(0)

#df_segunda["segunda-feira, 28 de julho de 2025"] = df_segunda["segunda-feira, 28 de julho de 2025"].fillna(df_segunda["segunda-feira, 21 de julho de 2025"] - df_segunda["segunda-feira, 4 de agosto de 2025"])

#print(df_segunda.head())
#print(df_segunda.isnull().sum())


# limpando planilha de terça
df_terca = df['TERÇAS']
df_terca = df_terca.drop_duplicates()

#print(df_terca.isnull().sum())

df_terca = df_terca.fillna(0) # transforma valores nulos de itens recentemente adicionados em 0

df_terca["terça-feira, 12 de agosto de 2025"] = df_terca["terça-feira, 12 de agosto de 2025"].fillna(df_terca["segunda-feira, 4 de agosto de 2025"])
df_terca["terça-feira, 27 de maio de 2025"] = df_terca["terça-feira, 27 de maio de 2025"].fillna(df_terca["terça-feira, 20 de maio de 2025"])
df_terca["terça-feira, 19 de agosto de 2025"] = df_terca["terça-feira, 19 de agosto de 2025"].fillna(df_terca["terça-feira, 12 de agosto de 2025"])


#limpando planilha de quarta
df_quarta = df['QUARTAS']
df_quarta = df_quarta.drop_duplicates()
#print(df_quarta.isnull().sum())

df_quarta = df_quarta.fillna(0)
df_quarta["quarta-feira, 2 de julho de 2025"] = df_quarta["quarta-feira, 2 de julho de 2025"].fillna(df_quarta[""])
