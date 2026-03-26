const API_BASE_URL = "/api";

const form = document.getElementById("productForm");
const productList = document.getElementById("productList");
const emptyState = document.getElementById("emptyState");
const feedback = document.getElementById("feedback");

const totalProdutos = document.getElementById("totalProdutos");
const valorCusto = document.getElementById("valorCusto");
const valorVenda = document.getElementById("valorVenda");
const lucroEstimado = document.getElementById("lucroEstimado");

function formatCurrency(value) {
  return new Intl.NumberFormat("pt-BR", {
    style: "currency",
    currency: "BRL",
  }).format(Number(value || 0));
}

function showFeedback(message) {
  feedback.textContent = message;
  feedback.classList.remove("hidden");
  setTimeout(() => feedback.classList.add("hidden"), 3000);
}

async function loadDashboard() {
  try {
    const response = await fetch(`${API_BASE_URL}/dashboard`);

    if (!response.ok) {
      throw new Error("Erro ao carregar dashboard.");
    }

    const data = await response.json();

    totalProdutos.textContent = data.total_produtos ?? 0;
    valorCusto.textContent = formatCurrency(data.valor_total_custo);
    valorVenda.textContent = formatCurrency(data.valor_total_venda);
    lucroEstimado.textContent = formatCurrency(data.lucro_estimado);
  } catch (error) {
    totalProdutos.textContent = "0";
    valorCusto.textContent = formatCurrency(0);
    valorVenda.textContent = formatCurrency(0);
    lucroEstimado.textContent = formatCurrency(0);
    showFeedback("Não foi possível carregar o dashboard.");
  }
}

function createProductCard(produto) {
  const article = document.createElement("article");
  article.className = "product-item";

  const imageHtml = produto.foto
    ? `<img src="/${produto.foto}" alt="Foto de ${produto.nome}" class="product-image" />`
    : `<div class="product-image placeholder">Sem foto</div>`;

  article.innerHTML = `
    <div class="product-image-wrapper">${imageHtml}</div>
    <div class="product-info">
      <div class="product-top-row">
        <div>
          <h3>${produto.nome}</h3>
        </div>
        <button type="button" class="delete-btn" data-id="${produto.id}">Excluir</button>
      </div>
      <div class="prices">
        <div>
          <span>Custo</span>
          <strong>${formatCurrency(produto.preco_pago)}</strong>
        </div>
        <div>
          <span>Margem</span>
          <strong>${Number(produto.margem_lucro || 0).toFixed(2)}%</strong>
        </div>
        <div>
          <span>Preço de venda</span>
          <strong>${formatCurrency(produto.preco_venda)}</strong>
        </div>
      </div>
    </div>
  `;

  article.querySelector(".delete-btn").addEventListener("click", async () => {
    await deleteProduct(produto.id);
  });

  return article;
}

async function loadProducts() {
  try {
    const response = await fetch(`${API_BASE_URL}/produtos`);

    if (!response.ok) {
      throw new Error("Erro ao carregar produtos.");
    }

    const produtos = await response.json();

    productList.innerHTML = "";

    if (!produtos.length) {
      emptyState.classList.remove("hidden");
    } else {
      emptyState.classList.add("hidden");
      produtos.forEach((produto) => {
        productList.appendChild(createProductCard(produto));
      });
    }
  } catch (error) {
    productList.innerHTML = "";
    emptyState.classList.remove("hidden");
    showFeedback("Não foi possível carregar os produtos.");
  }
}

async function deleteProduct(productId) {
  try {
    const response = await fetch(`${API_BASE_URL}/produtos/${productId}`, {
      method: "DELETE",
    });

    if (!response.ok) {
      throw new Error("Erro ao excluir produto.");
    }

    showFeedback("Produto excluído com sucesso.");
    await refreshScreen();
  } catch (error) {
    showFeedback("Não foi possível excluir o produto.");
  }
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  try {
    const formData = new FormData(form);

    const response = await fetch(`${API_BASE_URL}/produtos`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.detail || "Erro ao cadastrar produto.");
    }

    form.reset();
    showFeedback("Produto cadastrado com sucesso.");
    await refreshScreen();
  } catch (error) {
    showFeedback(error.message || "Erro ao cadastrar produto.");
  }
});

async function refreshScreen() {
  await Promise.all([loadDashboard(), loadProducts()]);
}

refreshScreen();
