from ..models import Categoria, Producto
from ..estructuras.arbol import ArbolCategorias
from ..estructuras.grafo import GrafoProductos

def inicializar_estructuras():
    arbol = ArbolCategorias()
    grafo = GrafoProductos()

    categorias = Categoria.objects.all()
    for c in categorias:
        arbol.insertar(c)

    productos = Producto.objects.select_related('categoria').all()

    for p in productos:
        grafo.agregar_producto(p.id)

    # Relación por categoría
    for p in productos:
        similares = productos.filter(categoria=p.categoria).exclude(id=p.id)
        for s in similares:
            grafo.relacionar(p.id, s.id)

    return arbol, grafo