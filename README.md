Automação RPA desenvolvida em Python para extração de dados de uma tabela em uma aplicação web e envio das informações para uma planilha do Google Sheets.

## Demonstração:
<img width="726" height="370" alt="Image" src="https://github.com/user-attachments/assets/84968435-c424-456f-8774-04503a18595b" />


## Como funciona

O fluxo da automação é dividido em algumas etapas:

```text
Abrir navegador
      ↓
Acessar aplicação web
      ↓
Localizar tabela
      ↓
Extrair dados
      ↓
Converter para DataFrame
      ↓
Tratar dados
      ↓
Autenticar no Google
      ↓
Enviar dados para Google Sheets
```

## Pré-requisitos

Antes de executar o projeto, é necessário ter:

* Python 3.10 ou superior;
* Google Cloud Project;
* Google Sheets API habilitada;
* Google Drive API habilitada;
* Uma Service Account;
* Uma planilha do Google Sheets compartilhada com o e-mail da Service Account.

## Instalação

Clone o repositório:

```bash
git clone (https://github.com/CodIguinhoDev/rpa-web-data-extraction)
```

Entre na pasta do projeto:

```bash
cd rpa-web-data-extractor
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

Ative o ambiente virtual no Linux:

```bash
source .venv/Scripts/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` baseado no `.env.example`:

```env
SHEETS_CREDENTIALS=config/credentials.json
```

Coloque o arquivo de credenciais da Service Account em:

```text
config/credentials.json
```

Também é necessário compartilhar a planilha do Google Sheets com o e-mail da Service Account, concedendo permissão de edição.

## Execução

Execute o projeto com:

```bash
python main.py
```

## Estrutura do projeto

```text
rpa-web-data-extractor/
├── src/
│   ├── config/
│   ├── services/
│   │   ├── fetcher.py
│   │   ├── google_auth.py
│   │   └── spreadsheet.py
│   ├── utils/
│   │   └── browser.py
│   ├── app.py
│   └── main.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Tecnologias utilizadas

* Python
* Selenium
* Pandas
* gspread
* Google Sheets API
* Google Drive API
