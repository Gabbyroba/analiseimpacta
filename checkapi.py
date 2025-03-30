import requests

# URL para obter a lista de deputados
url_deputados = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome'
resposta = requests.get(url_deputados)

if resposta.status_code == 200:
    dados_deputados = resposta.json().get('dados', [])
    if dados_deputados:
        # Seleciona o primeiro deputado da lista como exemplo
        deputado = dados_deputados[2]
        id_deputado = deputado['id']
        nome_deputado = deputado['nome']
        print(f"Deputado selecionado: {nome_deputado} (ID: {id_deputado})")
    else:
        print("Nenhum deputado encontrado.")
else:
    print(f"Erro ao acessar a API: {resposta.status_code}")

def obter_despesas(id_deputado, ano=2024):
    despesas = []
    pagina = 1
    while True:
        url_despesas = f'https://dadosabertos.camara.leg.br/api/v2/deputados/{id_deputado}/despesas?ano={ano}&itens=100&pagina={pagina}'
        resposta = requests.get(url_despesas)
        
        if resposta.status_code != 200:
            print(f"Erro ao acessar despesas do deputado {id_deputado}: {resposta.status_code}")
            break
        
        dados = resposta.json()
        despesas_pagina = dados.get('dados', [])
        despesas.extend(despesas_pagina)
        
        # Verifica se há mais páginas de resultados
        if not any(link['rel'] == 'next' for link in dados.get('links', [])):
            break
        pagina += 1
    
    return despesas

# Obtém as despesas do deputado selecionado
despesas = obter_despesas(id_deputado)

# Verifica se há despesas com valores negativos
despesas_negativas = [d for d in despesas if d['valorDocumento'] < 0 or d['valorLiquido'] < 0]

print(f"Total de despesas encontradas: {len(despesas)}")
print(f"Total de despesas com valores negativos: {len(despesas_negativas)}")