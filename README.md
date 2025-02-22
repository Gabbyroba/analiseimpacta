# Análise de Despesas de Deputados

Este projeto tem como objetivo coletar, processar e analisar dados das despesas de deputados federais no Brasil. Os dados são extraídos da API de Dados Abertos da Câmara dos Deputados e armazenados em um banco de dados SQLite. O projeto também contará com integração ao Power BI para criação de um dashboard interativo.

## 🚀 Tecnologias Utilizadas

- **Python** (para coleta e processamento dos dados)
- **Requests** (para fazer chamadas à API)
- **Pandas** (para manipulação e análise de dados)
- **SQLite** (para armazenamento dos dados)
- **TQDM** (para barra de progresso durante a coleta de dados)
- **Power BI** (para visualização e análise dos dados)

## 💂️ Estrutura do Projeto

```
📂 analise-despesas-deputados
│── 📄 .gitignore            # Arquivo para ignorar arquivos desnecessários no Git
│── 📄 README.md             # Documentação do projeto
│── 📄 despesas_deputados.db  # Banco de dados SQLite gerado pelo script
│── 📄 main.py               # Script principal para coleta e processamento dos dados
│── 📄 vertabela.py          # Script para visualizar os dados do banco
```

## 👅 Instalação e Execução

### 1⃣ Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/analise-despesas-deputados.git
cd analise-despesas-deputados
```

### 2⃣ Criar um Ambiente Virtual (Opcional, mas Recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

### 3⃣ Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4⃣ Executar o Script
```bash
python main.py
```

Isso iniciará a coleta dos dados e os armazenará em um banco de dados SQLite.

## 📊 Integração com Power BI

Após a execução do script, os dados coletados estarão disponíveis no arquivo `despesas_deputados.db`. Esse banco pode ser importado para o Power BI para criação de visualizações interativas.

### Passos para Importação no Power BI:
1. Abrir o Power BI.
2. Selecionar **Obter Dados** > **Banco de Dados SQLite**.
3. Conectar ao arquivo `despesas_deputados.db`.
4. Criar relatórios e dashboards interativos com os dados coletados.

## 📝 Considerações Finais

Este projeto faz parte de um trabalho acadêmico de Análise de Dados, podendo ser expandido para outras análises e fontes de dados no futuro. Sugestões e contribuições são bem-vindas! 😊