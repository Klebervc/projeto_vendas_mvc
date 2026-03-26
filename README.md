# Projeto de consulta de vendas com MVC, backend e frontend separados

Este projeto reorganiza a primeira versão em uma estrutura mais profissional:

- `backend/`: API FastAPI, banco SQLite e uploads
- `frontend/`: HTML, CSS e JavaScript da interface
- padrão MVC no backend:
  - `models/`: acesso aos dados
  - `controllers/`: regras da API e fluxo das requisições
  - `views/`: preparação dos dados exibidos no dashboard

## Estrutura

```text
projeto_vendas_mvc/
├── backend/
│   ├── app/
│   │   ├── controllers/
│   │   │   └── produto_controller.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── database.py
│   │   ├── models/
│   │   │   └── produto_model.py
│   │   ├── views/
│   │   │   └── produto_view.py
│   │   └── main.py
│   ├── uploads/
│   ├── requirements.txt
│   └── .gitignore
├── frontend/
│   ├── index.html
│   └── static/
│       ├── app.js
│       └── styles.css
└── README.md
```

## Como executar

### 1. Entrar na pasta do backend

```bash
cd backend
```

### 2. Criar e ativar a venv

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar a API

```bash
uvicorn app.main:app --reload
```

### 5. Abrir no navegador

```text
http://127.0.0.1:8000
```

## Como o MVC ficou aplicado

### Model
`backend/app/models/produto_model.py`
- fala com o SQLite
- lista, cria, busca e exclui produtos

### Controller
`backend/app/controllers/produto_controller.py`
- recebe as requisições
- valida o nome
- calcula o preço de venda
- salva foto
- chama o model

### View
`backend/app/views/produto_view.py`
- prepara os dados agregados do dashboard
- total de produtos
- custo total
- venda total estimada
- lucro bruto estimado

## Observações

- O arquivo `backend/produtos.db` é criado automaticamente na primeira execução.
- As imagens ficam em `backend/uploads/`.
- O frontend conversa com a API via JavaScript usando `/api/produtos` e `/api/dashboard`.
