import pandas as pd

databases = ['SEGUNDAS','TERÇAS','QUARTAS','QUINTAS','SEXTAS']
df = pd.read_excel(r"analise_estoque\database\database_contagem.xlsx", sheet_name=databases)

# limpando planilha de segunda
df_segunda = df['SEGUNDAS']
df_segunda = df_segunda.drop_duplicates()

# itens null nao estavam na contagem
df_segunda["segunda-feira, 5 de maio de 2025"] = df_segunda['segunda-feira, 5 de maio de 2025'].fillna(0)
df_segunda["segunda-feira, 12 de maio de 2025"] = df_segunda['segunda-feira, 12 de maio de 2025'].fillna(0)
df_segunda["segunda-feira, 19 de maio de 2025"] = df_segunda['segunda-feira, 19 de maio de 2025'].fillna(0)

df_segunda["segunda-feira, 28 de julho de 2025"] = df_segunda["segunda-feira, 28 de julho de 2025"].fillna(df_segunda["segunda-feira, 21 de julho de 2025"] - df_segunda["segunda-feira, 4 de agosto de 2025"])

#print(df_segunda.head())
#print(df_segunda.isnull().sum())

# limpando planilha de terça

df_terca = df['TERÇAS']
df_terca = df_terca.drop_duplicates()