from typing import Any

def montar_dashboard(produtos: list[dict[str, Any]]) -> dict[str, Any]:
    total_produtos = len(produtos)

    valor_total_custo = round(
        sum(float(produto.get("preco_pago") or 0) for produto in produtos),
        2
    )

    valor_total_venda = round(
        sum(float(produto.get("preco_venda") or 0) for produto in produtos),
        2
    )

    lucro_estimado = round(valor_total_venda - valor_total_custo, 2)

    return {
        "produtos": produtos,
        "total_produtos": total_produtos,
        "valor_total_custo": valor_total_custo,
        "valor_total_venda": valor_total_venda,
        "lucro_estimado": lucro_estimado,
    }
