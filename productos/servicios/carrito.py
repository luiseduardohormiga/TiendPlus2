# productos/servicios/carrito.py
def obtener_carrito(request):
    return request.session.get("cart", [])

def agregar_al_carrito(request, producto_id):
    cart = obtener_carrito(request)
    if producto_id not in cart:
        cart.append(producto_id)
    request.session["cart"] = cart
    return cart

def vaciar_carrito(request):
    request.session["cart"] = []
