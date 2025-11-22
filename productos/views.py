from django.shortcuts import render
from django.http import Http404

# Lista de productos simulada (ejemplo)
PRODUCTOS = [
    {"id": 1, "nombre": "Smartphone Samsung", "precio": 1200, "descripcion": "Teléfono de última generación", "imagen": "productos/Smartphone_Samsung_A34.jpeg"},
    {"id": 2, "nombre": "Laptop HP Pavilion", "precio": 2500, "descripcion": "Laptop potente para trabajo y estudio", "imagen": "productos/Laptop_HP_Pavilion_14.jpeg"},
    {"id": 3, "nombre": "Audífonos Inalámbricos", "precio": 300, "descripcion": "Sonido envolvente y batería duradera", "imagen": "productos/Audífonos_Inalámbricos_JBL_Tune_510BT.webp"},
    {"id": 4, "nombre": "Mouse Gamer Logitech G203", "precio": 150, "descripcion": "Mouse gamer con alta precisión", "imagen": "productos/Mouse_Gamer_Logitech_G203.webp"},
]

def lista_productos(request):
    q = request.GET.get("q", "")
    productos = [p for p in PRODUCTOS if q.lower() in p["nombre"].lower()]
    return render(request, "productos/lista_productos.html", {"productos": productos, "q": q})

def detalle_view(request, producto_id):
    producto = next((p for p in PRODUCTOS if p["id"] == producto_id), None)
    if not producto:
        raise Http404("Producto no encontrado")

    # Recomendaciones: otros productos distintos al actual
    recomendaciones = [p for p in PRODUCTOS if p["id"] != producto_id][:3]

    return render(request, "productos/detalle.html", {
        "producto": producto,
        "recomendaciones": recomendaciones
    })

def ver_carrito_view(request):
    carrito = request.session.get("carrito", [])
    productos = [p for p in PRODUCTOS if p["id"] in carrito]
    return render(request, "productos/ver_carrito.html", {"productos": productos})

def add_to_cart_view(request, producto_id):
    carrito = request.session.get("carrito", [])
    if producto_id not in carrito:
        carrito.append(producto_id)
    request.session["carrito"] = carrito
    return render(request, "productos/ver_carrito.html", {"productos": [p for p in PRODUCTOS if p["id"] in carrito]})

def vaciar_carrito_view(request):
    request.session["carrito"] = []
    return render(request, "productos/ver_carrito.html", {"productos": []})
