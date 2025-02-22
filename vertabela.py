import sqlite3
import pandas as pd

# Conectar ao banco de dados
con = sqlite3.connect("despesas_deputados.db")

# Verificar as tabelas existentes
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tabelas no banco de dados:", cursor.fetchall())

# Carregar a tabela em um DataFrame e visualizar as primeiras linhas
df = pd.read_sql("SELECT * FROM despesas LIMIT 5;", con)
print(df)

# Fechar a conexão
con.close()