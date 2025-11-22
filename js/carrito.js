// ARCHIVO: static/js/carrito.js

function toggleCart(open = true) {
    const sidebar = document.getElementById("cartSidebar");
    const overlay = document.getElementById("cartOverlay");

    if (open) {
        sidebar.classList.add("open");
        overlay.classList.remove("d-none");
    } else {
        sidebar.classList.remove("open");
        overlay.classList.add("d-none");
    }
}

function showToast(message) {
    let toast = document.createElement("div");
    toast.className = "toast-alert";
    toast.textContent = message;

    document.body.appendChild(toast);

    setTimeout(() => toast.classList.add("show"), 50);
    setTimeout(() => {
        toast.classList.remove("show");
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

function addToCart(productId) {
    fetch(`/producto/${productId}/add/ajax/`)
        .then(response => response.json())
        .then(data => {
            showToast(data.message);
            document.getElementById("cartSidebar").innerHTML = data.sidebar_html;
            toggleCart(true);
        })
        .catch(error => console.error("Error en AJAX:", error));
}

function vaciarCarrito() {
    fetch(`/carrito/vaciar/`)
        .then(response => response.json())
        .then(data => {
            showToast(data.message);
            document.getElementById("cartSidebar").innerHTML = data.sidebar_html;
        })
        .catch(error => console.error("Error al vaciar carrito:", error));
}
