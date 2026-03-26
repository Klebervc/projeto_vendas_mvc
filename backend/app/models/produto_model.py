from typing import Any
from app.core.database import get_connection

class ProdutoModel:
    @staticmethod
    def listar_produtos() -> list[dict[str, Any]]:
        conn = get_connection()
        produtos = conn.execute(
            """
            SELECT id, nome, foto, preco_pago, margem_lucro, preco_venda
            FROM produtos
            ORDER BY id DESC
            """
        ).fetchall()
        conn.close()

        return [dict(produto) for produto in produtos]

    @staticmethod
    def criar_produto(
        nome: str,
        foto: str | None,
        preco_pago: float,
        margem_lucro: float,
        preco_venda: float,
    ) -> int:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO produtos (nome, foto, preco_pago, margem_lucro, preco_venda)
            VALUES (?, ?, ?, ?, ?)
            """,
            (nome, foto, preco_pago, margem_lucro, preco_venda),
        )

        conn.commit()
        produto_id = cursor.lastrowid
        conn.close()

        return produto_id

    @staticmethod
    def buscar_produto(produto_id: int) -> dict[str, Any] | None:
        conn = get_connection()
        produto = conn.execute(
            """
            SELECT id, nome, foto, preco_pago, margem_lucro, preco_venda
            FROM produtos
            WHERE id = ?
            """,
            (produto_id,),
        ).fetchone()
        conn.close()

        return dict(produto) if produto else None

    @staticmethod
    def excluir_produto(produto_id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
        conn.commit()

        removido = cursor.rowcount > 0
        conn.close()

        return removido
