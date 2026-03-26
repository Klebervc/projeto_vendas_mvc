from pathlib import Path
import os

# Caminho da pasta backend
BACKEND_DIR = Path(__file__).resolve().parents[2]

# Caminho da raiz do projeto
PROJECT_DIR = BACKEND_DIR.parent

# Caminho da pasta frontend
FRONTEND_DIR = PROJECT_DIR / "frontend"

# Pasta persistente:
# em produção pode ser algo como /data
# localmente, se a variável não existir, usa a própria pasta backend
PERSISTENT_DATA_DIR = Path(os.getenv("PERSISTENT_DATA_DIR", str(BACKEND_DIR)))
PERSISTENT_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Caminho do banco
DB_PATH = PERSISTENT_DATA_DIR / "produtos.db"

# Caminho da pasta de uploads
UPLOAD_DIR = PERSISTENT_DATA_DIR / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Caminho dos arquivos estáticos do frontend
STATIC_DIR = FRONTEND_DIR / "static"

# Caminho do arquivo principal do frontend
INDEX_FILE = FRONTEND_DIR / "index.html"
