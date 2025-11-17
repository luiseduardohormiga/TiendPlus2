from django.shortcuts import get_object_or_404
from ..models import Producto

CART_SESSION_ID = "cart_items"  # almacena lista de producto_ids

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    cart = request.session.get(CART_SESSION_ID, [])
    cart.append(producto.id)
    # evitar duplicados si quieres: cart = list(dict.fromkeys(cart))
    request.session[CART_SESSION_ID] = cart
    request.session.modified = True
    return cart

def obtener_carrito(request):
    from ..models import Producto
    cart = request.session.get(CART_SESSION_ID, [])
    productos = Producto.objects.filter(id__in=cart)
    # mantener orden del cart
    ordenados = sorted(productos, key=lambda p: cart.index(p.id))
    return ordenados