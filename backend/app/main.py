from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.controllers.produto_controller import router as produto_router
from app.core.config import UPLOAD_DIR, STATIC_DIR, INDEX_FILE
from app.core.database import init_db

app = FastAPI(title="Consulta de Vendas de Produtos - MVC")

init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(produto_router, prefix="/api", tags=["produtos"])

app.mount("/uploads", StaticFiles(directory=str(UPLOAD_DIR)), name="uploads")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
def serve_index():
    return FileResponse(INDEX_FILE)
