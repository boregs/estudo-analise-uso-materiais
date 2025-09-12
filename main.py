import pandas as pd

<<<<<<< HEAD
# ---- 

=======
>>>>>>> f914c37b9860667a7f9a7f6b337660c3e5208591
databases = ['SEGUNDAS','TERCAS','QUARTAS','QUINTAS','SEXTAS']
df = pd.read_excel(r"database\DATABASE_ATUALIZADA.xlsx", sheet_name=databases)
df_segunda = df['SEGUNDAS']

<<<<<<< HEAD
# ---- limpando planilha de segunda ----
=======
# limpando planilha de segunda
>>>>>>> f914c37b9860667a7f9a7f6b337660c3e5208591

df_segunda = df['SEGUNDAS']
df_segunda = df_segunda.drop_duplicates()

# itens null nao estavam na contagem
df_segunda["segunda-feira, 5 de maio de 2025"] = df_segunda['segunda-feira, 5 de maio de 2025'].fillna(0)
df_segunda["segunda-feira, 12 de maio de 2025"] = df_segunda['segunda-feira, 12 de maio de 2025'].fillna(0)
df_segunda["segunda-feira, 19 de maio de 2025"] = df_segunda['segunda-feira, 19 de maio de 2025'].fillna(0)

#df_segunda["segunda-feira, 28 de julho de 2025"] = df_segunda["segunda-feira, 28 de julho de 2025"].fillna(df_segunda["segunda-feira, 21 de julho de 2025"] - df_segunda["segunda-feira, 4 de agosto de 2025"])

#print(df_segunda.head())
#print(df_segunda.isnull().sum())


<<<<<<< HEAD
# ---- limpando planilha de terça ----
df_terca = df['TERCAS']
=======
# limpando planilha de terça
df_terca = df['TERÇAS']
>>>>>>> f914c37b9860667a7f9a7f6b337660c3e5208591
df_terca = df_terca.drop_duplicates()

#print(df_terca.isnull().sum())

df_terca = df_terca.fillna(0) # transforma valores nulos de itens recentemente adicionados em 0

df_terca["terça-feira, 12 de agosto de 2025"] = df_terca["terça-feira, 12 de agosto de 2025"].fillna(df_terca["segunda-feira, 4 de agosto de 2025"])
df_terca["terça-feira, 27 de maio de 2025"] = df_terca["terça-feira, 27 de maio de 2025"].fillna(df_terca["terça-feira, 20 de maio de 2025"])
df_terca["terça-feira, 19 de agosto de 2025"] = df_terca["terça-feira, 19 de agosto de 2025"].fillna(df_terca["terça-feira, 12 de agosto de 2025"])


<<<<<<< HEAD
# ---- limpando planilha de quarta ----
df_quarta = df['QUARTAS']
df_quarta = df_quarta.drop_duplicates()
#print(df_quarta.isnull().sum())
   
#print(df_quarta["quarta-feira, 28 de maio de 2025"].tail(10))
#print(df_quarta["quarta-feira, 2 de julho de 2025"].tail(10))
#print(df_quarta["quarta-feira, 25 de junho de 2025"].tail(10))

df_quarta["quarta-feira, 4 de junho de 2025"] = df_quarta["quarta-feira, 4 de junho de 2025"].fillna(df_quarta["quarta-feira, 28 de maio de 2025"])
df_quarta["quarta-feira, 2 de julho de 2025"] = df_quarta["quarta-feira, 2 de julho de 2025"].fillna(df_quarta["quarta-feira, 25 de junho de 2025"])
#print(df_quarta["quarta-feira, 23 de julho de 2025"].tail(10))

df_quarta["quarta-feira, 9 de julho de 2025"] = df_quarta["quarta-feira, 9 de julho de 2025"].fillna(df_quarta["quarta-feira, 2 de julho de 2025"] - 1400)
#print(df_quarta["quarta-feira, 9 de julho de 2025"].tail(10))
df_quarta["quarta-feira, 16 de julho de 2025"] = df_quarta["quarta-feira, 16 de julho de 2025"].fillna(df_quarta["quarta-feira, 9 de julho de 2025"] - 1400)
#print(df_quarta["quarta-feira, 16 de julho de 2025"].tail(10))
#print(df_quarta.isnull().sum())
df_quarta = df_quarta.fillna(0)
#print(df_quarta.isnull().sum())

# ---- limpando planilha de quinta ----
# PLANILHA SEM DADOS FALTANDO

df_quinta = df["QUINTAS"]
df_quinta = df_quinta.drop_duplicates()
#print(df_quinta.isnull().sum())
#Wprint(df_quinta.head(30))



# ---- limpando planilha de sexta ----

df_sexta = df["SEXTAS"]
df_sexta  = df_sexta .drop_duplicates()
#print(df_sexta.isnull().sum())
#print(df_sexta.tail(30))
#print(df_sexta["sexta-feira, 1 de agosto de 2025"].head(30))
#print(df_sexta["sexta-feira, 25 de julho de 2025"].head(30))
#print(df_sexta["quinta-feira, 10 de julho de 2025"].head(30))
df_sexta = df_sexta.fillna(0)
##print(df_sexta.isnull().sum())


# ---- criando uma nova database limpa para analise e criação de dashboard ----

database_final = "database_limpa.xlsx"
writer = pd.ExcelWriter(database_final, engine="xlsxwriter")

dataframes_dos_dias = {
    'SEGUNDAS' : df_segunda,
    'TERCAS' : df_terca,
    'QUARTAS' : df_quarta,
    'QUINTAS' : df_quinta,
    'SEXTAS' : df_sexta
}

for name_aba, df in dataframes_dos_dias.items():
    df.to_excel(writer,sheet_name=name_aba, index=False)

writer.close()
=======
#limpando planilha de quarta
df_quarta = df['QUARTAS']
df_quarta = df_quarta.drop_duplicates()
#print(df_quarta.isnull().sum())

df_quarta = df_quarta.fillna(0)
df_quarta["quarta-feira, 2 de julho de 2025"] = df_quarta["quarta-feira, 2 de julho de 2025"].fillna(df_quarta[""])
>>>>>>> f914c37b9860667a7f9a7f6b337660c3e5208591
