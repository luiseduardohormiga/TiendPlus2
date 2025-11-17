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
    # inicializar nodos del grafo
    for p in productos:
        grafo.agregar_producto(p.id)

    # Estrategia básica de relaciones:
    # (1) Relacionar productos de la misma categoría
    # (2) Relacionar manuales / basadas en reglas (si quieres)
    for p in productos:
        # relacionar con otros de misma categoría
        similares = productos.filter(categoria=p.categoria).exclude(id=p.id)
        for s in similares:
            grafo.relacionar(p.id, s.id)

    # TODO: si tienes datos históricos de compras, relaciona según co-ocurrencia
    return arbol, grafo