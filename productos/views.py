from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria
from .servicios.inicializador import inicializar_estructuras
from .servicios.carrito import agregar_al_carrito, obtener_carrito

def lista_productos(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, "productos/lista.html", {"productos": productos, "categorias": categorias})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "productos/detalle.html", {"producto": producto})

def add_to_cart_and_recommend(request, pk):
    # 1) agregamos al carrito en session
    cart = agregar_al_carrito(request, pk)

    # 2) inicializamos grafo (puede optimizarse con caché)
    _, grafo = inicializar_estructuras()

    # 3) pedimos recomendaciones nivel 1 (vecinos directos)
    recomend_ids = grafo.recomendar_nivel(pk, niveles=1)
    # quitamos los que ya están en el carrito
    recomend_ids = [rid for rid in recomend_ids if rid not in cart]

    # 4) recuperamos objetos
    from .models import Producto
    recomendaciones = Producto.objects.filter(id__in=recomend_ids)

    return render(request, "productos/recomendaciones_modal.html", {
        "producto_actual": Producto.objects.get(pk=pk),
        "recomendaciones": recomendaciones,
        "cart": obtener_carrito(request)
    })