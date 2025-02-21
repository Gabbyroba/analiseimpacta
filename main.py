import requests
import pandas as pd
import sqlite3

# Função para obter dados dos deputados
def obter_deputados():
    url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome'
    resposta = requests.get(url)
    
    if resposta.status_code != 200:
        print(f"Erro ao acessar API: {resposta.status_code}")
        return []
    
    try:
        return resposta.json().get('dados', [])
    except requests.exceptions.JSONDecodeError:
        print("Erro ao decodificar JSON da resposta da API.")
        return []

# Função para obter despesas de um deputado específico
def obter_despesas(id_deputado, ano=2024):
    despesas = []
    pagina = 1
    while True:
        url = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputado}/despesas?ano={ano}&itens=100&pagina={pagina}'
        resposta = requests.get(url)
        
        if resposta.status_code != 200:
            print(f"Erro ao acessar despesas do deputado {id_deputado}: {resposta.status_code}")
            break
        
        try:
            dados = resposta.json()
            despesas.extend(dados.get('dados', []))
        except requests.exceptions.JSONDecodeError:
            print(f"Erro ao decodificar JSON das despesas do deputado {id_deputado}.")
            break
        
        if not any(link['rel'] == 'next' for link in dados.get('links', [])):
            break
        pagina += 1
    
    return despesas

# Obtém a lista de deputados
deputados = obter_deputados()
df_deputados = pd.DataFrame(deputados)

# Lista para armazenar as despesas
despesas_totais = []
dados_deputados = []

# Obtém despesas para cada deputado
for deputado in (deputados):
    id_deputado = deputado['id']
    despesas = obter_despesas(id_deputado)
    despesas_totais.extend(despesas)
    
    # Armazena os dados do deputado
    if despesas:
        dados_deputados.extend([
            [
                deputado['nome'], deputado['siglaPartido'], deputado['siglaUf'],
                deputado['idLegislatura'], deputado['urlFoto'], deputado.get('email', '')
            ] for _ in despesas
        ])

# Cria DataFrames
df_despesas = pd.DataFrame(despesas_totais)
df_dados_deputados = pd.DataFrame(dados_deputados, columns=['nome', 'siglaPartido', 'siglaUF', 'idLegislatura', 'foto', 'email'])

if not df_despesas.empty and not df_dados_deputados.empty:
    df_final = df_dados_deputados.join(df_despesas)
    print("Merge criado com sucesso!")

    # Salva os dados em um banco de dados SQLite
    con = sqlite3.connect('despesas_deputados.db')
    df_final.to_sql('despesas', con, if_exists='replace', index=False)
    print("Conexão bem sucedida, tabela criada!")
    con.close()
else:
    print("Nenhum dado válido foi coletado.")
