from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria
from .servicios.inicializador import inicializar_estructuras
from .servicios.carrito import agregar_al_carrito, obtener_carrito
from .árbol_categorias import ArbolCategorias
from django.http import JsonResponse
from django.template.loader import render_to_string

def lista_productos(request):
    productos = Producto.objects.all()

    # cargar categorías en el árbol
    arbol = ArbolCategorias()
    for c in Categoria.objects.all():
        arbol.insertar(c)

    categorias_ordenadas = arbol.ordenar()
    
    # filtrado por categoría si se envía por GET
    categoria_id = request.GET.get("categoria")
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    return render(request, "productos/lista_productos.html", {
        "productos": productos,
        "categorias": categorias_ordenadas
    })

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "productos/detalle.html", {"producto": producto})

def add_to_cart_and_recommend(request, pk):
    # 1. Agregar al carrito
    cart = agregar_al_carrito(request, pk)

    # 2. Inicializar estructuras
    _, grafo = inicializar_estructuras()

    # 3. Recomendaciones (vecinos directos)
    recomend_ids = grafo.recomendar_nivel(pk, niveles=1)

    # Evitar duplicados del carrito
    recomend_ids = [r for r in recomend_ids if r not in cart]

    productos = Producto.objects.filter(id__in=recomend_ids)

    return render(request, "productos/recomendaciones_modal.html", {
        "producto_actual": Producto.objects.get(id=pk),
        "recomendaciones": productos,
        "cart": obtener_carrito(request)
    })
    
def add_to_cart_ajax(request, pk):
    cart = agregar_al_carrito(request, pk)

    sidebar_html = render_to_string("cart/sidebar.html", request=request)

    return JsonResponse({
        "message": "Producto añadido al carrito",
        "sidebar_html": sidebar_html
    })