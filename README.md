# Projeto Vendas MVC

Aplicação web para **cadastro e consulta de produtos**, com cálculo automático de preço de venda, upload de imagens, dashboard resumido e persistência em **SQLite**.

O projeto foi organizado em **arquitetura MVC**, com **FastAPI** no backend e **HTML/CSS/JavaScript** no frontend. O backend também serve o frontend, então toda a aplicação roda em **um único servidor**.

---

## Funcionalidades

- Cadastro de produtos com:
  - nome
  - foto
  - preço pago
  - margem de lucro (%)
- Cálculo automático do preço de venda
- Listagem de produtos cadastrados
- Exclusão de produtos
- Dashboard com:
  - total de produtos
  - custo total
  - venda total estimada
  - lucro bruto estimado
- Persistência em banco SQLite
- Armazenamento de imagens em pasta de uploads

---

## Stack utilizada

### Backend
- Python
- FastAPI
- Uvicorn
- SQLite

### Frontend
- HTML
- CSS
- JavaScript

### Arquitetura
- MVC

---

## Estrutura do projeto

```text
PROJETO_VENDAS_MVC/
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
│   ├── produtos.db
│   ├── requirements.txt
│   └── .gitignore
├── frontend/
│   ├── static/
│   │   ├── app.js
│   │   └── styles.css
│   └── index.html
└── README.md
```

---

## Como a aplicação funciona

### Fluxo do usuário

1. O usuário abre o sistema no navegador.
2. O FastAPI entrega o `index.html` na rota `/`.
3. O frontend carrega os arquivos estáticos em `/static`.
4. O usuário preenche o formulário com os dados do produto.
5. O JavaScript envia os dados para `POST /api/produtos`.
6. O backend valida os dados, calcula o preço de venda e salva a imagem.
7. O produto é gravado no banco SQLite.
8. O frontend atualiza a lista de produtos e o dashboard.

### Fluxo técnico

- `/` entrega a página principal.
- `/static/...` entrega CSS e JavaScript.
- `/uploads/...` entrega as imagens salvas.
- `/api/...` expõe os endpoints da aplicação.

Isso elimina a necessidade de rodar frontend e backend separadamente em portas diferentes.

---

## Arquitetura MVC

### Model
Responsável pelo acesso ao banco de dados.

Arquivo principal:
- `backend/app/models/produto_model.py`

### View
Responsável por montar a estrutura de dados do dashboard.

Arquivo principal:
- `backend/app/views/produto_view.py`

### Controller
Responsável por receber requisições HTTP e coordenar o fluxo da aplicação.

Arquivo principal:
- `backend/app/controllers/produto_controller.py`

### Core
Responsável por configuração e infraestrutura do projeto.

Arquivos:
- `backend/app/core/config.py`
- `backend/app/core/database.py`

### Main
Ponto de entrada da aplicação.

Arquivo:
- `backend/app/main.py`

---

## Explicação dos arquivos

### `backend/app/main.py`
Ponto de entrada da aplicação.

Responsabilidades:
- criar o app FastAPI
- inicializar o banco
- configurar CORS
- registrar rotas da API
- expor `/uploads`
- expor `/static`
- servir o `index.html` em `/`

---

### `backend/app/core/config.py`
Centraliza os caminhos principais do projeto.

Responsabilidades:
- localizar as pastas do projeto
- definir caminho do frontend
- definir caminho do banco SQLite
- definir caminho da pasta de uploads
- definir caminho da pasta de arquivos estáticos
- dar suporte a `PERSISTENT_DATA_DIR` para deploy

---

### `backend/app/core/database.py`
Camada de infraestrutura do banco.

Responsabilidades:
- abrir conexão com o SQLite
- configurar `row_factory`
- criar a tabela `produtos` se não existir

---

### `backend/app/models/produto_model.py`
Camada de acesso a dados.

Responsabilidades:
- listar produtos
- criar produto
- buscar produto por id
- excluir produto

---

### `backend/app/views/produto_view.py`
Camada de apresentação de dados do dashboard.

Responsabilidades:
- contar total de produtos
- somar custo total
- somar valor total de venda
- calcular lucro estimado
- montar o objeto de resposta do dashboard

---

### `backend/app/controllers/produto_controller.py`
Camada de controle HTTP.

Responsabilidades:
- definir as rotas de produtos
- validar dados recebidos
- calcular preço de venda
- salvar foto do produto
- cadastrar produto no banco
- listar produtos
- gerar dashboard
- excluir produto e foto correspondente

---

### `frontend/index.html`
Estrutura principal da interface.

Responsabilidades:
- exibir cabeçalho e descrição do sistema
- mostrar cards do dashboard
- mostrar formulário de cadastro
- mostrar área de feedback
- mostrar lista de produtos cadastrados

---

### `frontend/static/app.js`
Lógica dinâmica do frontend.

Responsabilidades:
- enviar formulário para a API
- carregar produtos
- carregar dashboard
- renderizar cards de produtos
- excluir produtos
- mostrar feedback visual
- formatar moeda em reais

---

### `frontend/static/styles.css`
Estilos da interface.

Responsabilidades:
- definir layout da página
- estilizar cards, formulário e listagem
- melhorar legibilidade e aparência visual
- tratar estados visuais como feedback e lista vazia

---

### `backend/requirements.txt`
Lista de dependências Python necessárias para rodar a aplicação.

Exemplo:
- `fastapi`
- `uvicorn`
- `python-multipart`

---

### `backend/produtos.db`
Arquivo físico do banco SQLite.

Armazena:
- id
- nome
- foto
- preço pago
- margem de lucro
- preço de venda

---

### `backend/uploads/`
Pasta onde ficam as imagens enviadas pelos usuários.

---

## Rotas principais

### Página principal
```text
GET /
```
Abre o frontend.

### Arquivos estáticos
```text
GET /static/styles.css
GET /static/app.js
```
Servem CSS e JavaScript.

### Uploads
```text
GET /uploads/nome_da_imagem.jpg
```
Servem as imagens dos produtos.

### API - listar produtos
```text
GET /api/produtos
```
Retorna a lista de produtos.

### API - cadastrar produto
```text
POST /api/produtos
```
Recebe os dados do formulário e cadastra um novo produto.

### API - excluir produto
```text
DELETE /api/produtos/{produto_id}
```
Exclui um produto e sua imagem, se existir.

### API - dashboard
```text
GET /api/dashboard
```
Retorna os totais consolidados da aplicação.

---

## Regra de negócio principal

O preço de venda é calculado com a fórmula:

```python
preco_venda = preco_pago * (1 + margem_lucro / 100)
```

### Exemplo
- preço pago: `100`
- margem de lucro: `30%`
- preço de venda: `130`

---

## Como instalar o projeto

### 1. Clonar o repositório
```bash
git clone URL_DO_REPOSITORIO
```

### 2. Entrar na pasta do projeto
```bash
cd PROJETO_VENDAS_MVC
```

### 3. Entrar na pasta do backend
```bash
cd backend
```

### 4. Criar ambiente virtual
```bash
python -m venv venv
```

### 5. Ativar ambiente virtual no Windows
```bash
venv\Scripts\activate
```

### 6. Instalar dependências
```bash
pip install -r requirements.txt
```

Se necessário:

```bash
pip install python-multipart
```

---

## Como executar localmente

Ainda dentro da pasta `backend`, rode:

```bash
uvicorn app.main:app --reload
```

Depois abra no navegador:

```text
http://127.0.0.1:8000
```

---

## Comandos principais

### Criar ambiente virtual
```bash
python -m venv venv
```

### Ativar ambiente virtual no Windows
```bash
venv\Scripts\activate
```

### Instalar dependências
```bash
pip install -r requirements.txt
```

### Rodar a aplicação
```bash
uvicorn app.main:app --reload
```

---

## Como testar a aplicação

1. Acesse `http://127.0.0.1:8000`
2. Preencha o formulário com os dados do produto
3. Envie uma foto, se desejar
4. Clique em **Cadastrar produto**
5. Verifique o item aparecendo na lista
6. Verifique o dashboard sendo atualizado
7. Teste a exclusão de um produto

---

## Resumo do fluxo da aplicação

### Cadastro
1. usuário envia formulário
2. frontend envia `FormData` para a API
3. backend valida os dados
4. backend calcula preço de venda
5. backend salva a imagem
6. backend grava os dados no SQLite
7. frontend recarrega lista e dashboard

### Listagem
1. frontend chama `GET /api/produtos`
2. backend consulta o banco
3. frontend renderiza os cards

### Dashboard
1. frontend chama `GET /api/dashboard`
2. backend lista produtos
3. view consolida os valores
4. frontend mostra os indicadores

### Exclusão
1. frontend chama `DELETE /api/produtos/{id}`
2. backend busca o produto
3. backend remove a foto do disco
4. backend remove o registro do banco
5. frontend atualiza a tela

---

## Resumo final

O **Projeto Vendas MVC** é uma aplicação web completa para cadastro e consulta de produtos, com persistência em SQLite, upload de imagens e arquitetura organizada em MVC.

O principal diferencial da versão final é que o **backend serve o frontend**, permitindo que toda a aplicação rode em um único servidor, simplificando o uso local e o deploy em nuvem.

### Em resumo, o sistema:
- cadastra produtos
- calcula preço de venda automaticamente
- salva dados no banco
- salva fotos no disco
- lista produtos cadastrados
- exibe indicadores de negócio
- permite exclusão de produtos

---

## Melhorias futuras

- edição de produtos
- busca por nome
- filtros
- paginação
- autenticação de usuários
- exportação para Excel
- migração para PostgreSQL
- deploy com armazenamento persistente em nuvem
