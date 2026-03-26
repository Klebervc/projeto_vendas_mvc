import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from fastapi.responses import RedirectResponse

from app.core.config import UPLOAD_DIR
from app.models.produto_model import ProdutoModel
from app.views.produto_view import montar_dashboard

router = APIRouter()


def calcular_preco_venda(preco_pago: float, margem_lucro: float) -> float:
    return round(preco_pago * (1 + margem_lucro / 100), 2)


def salvar_foto(foto: UploadFile | None) -> str | None:
    if not foto or not foto.filename:
        return None

    extensao = Path(foto.filename).suffix.lower()
    nome_arquivo = f"{uuid4().hex}{extensao}"
    destino = UPLOAD_DIR / nome_arquivo

    with destino.open("wb") as buffer:
        shutil.copyfileobj(foto.file, buffer)

    # caminho público relativo usado pelo frontend
    return f"uploads/{nome_arquivo}"


def excluir_foto(caminho_relativo_foto: str | None) -> None:
    if not caminho_relativo_foto:
        return

    nome_arquivo = Path(caminho_relativo_foto).name
    caminho_fisico = UPLOAD_DIR / nome_arquivo

    if caminho_fisico.exists():
        caminho_fisico.unlink()


@router.get("/produtos")
def listar_produtos() -> list[dict]:
    return ProdutoModel.listar_produtos()


@router.get("/dashboard")
def obter_dashboard() -> dict:
    produtos = ProdutoModel.listar_produtos()
    return montar_dashboard(produtos)


@router.post("/produtos")
async def cadastrar_produto(
    nome: str = Form(...),
    preco_pago: float = Form(...),
    margem_lucro: float = Form(...),
    foto: UploadFile | None = File(default=None),
):
    nome = nome.strip()

    if not nome:
        raise HTTPException(status_code=400, detail="Nome do produto é obrigatório.")

    if preco_pago <= 0:
        raise HTTPException(status_code=400, detail="O preço pago deve ser maior que zero.")

    if margem_lucro < 0:
        raise HTTPException(status_code=400, detail="A margem de lucro não pode ser negativa.")

    preco_venda = calcular_preco_venda(preco_pago, margem_lucro)
    foto_relativa = salvar_foto(foto)

    ProdutoModel.criar_produto(
        nome=nome,
        foto=foto_relativa,
        preco_pago=preco_pago,
        margem_lucro=margem_lucro,
        preco_venda=preco_venda,
    )

    return {
        "mensagem": "Produto cadastrado com sucesso.",
        "nome": nome,
        "preco_pago": preco_pago,
        "margem_lucro": margem_lucro,
        "preco_venda": preco_venda,
        "foto": foto_relativa,
    }


@router.delete("/produtos/{produto_id}")
def excluir_produto(produto_id: int):
    produto = ProdutoModel.buscar_produto(produto_id)

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado.")

    excluir_foto(produto.get("foto"))
    ProdutoModel.excluir_produto(produto_id)

    return {"mensagem": "Produto removido com sucesso."}


@router.post("/produtos/{produto_id}/excluir")
def excluir_produto_form(produto_id: int):
    produto = ProdutoModel.buscar_produto(produto_id)

    if produto:
        excluir_foto(produto.get("foto"))
        ProdutoModel.excluir_produto(produto_id)

    return RedirectResponse(url="/", status_code=303)
