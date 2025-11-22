from productos.models import Producto
from productos.estructuras.grafo import GrafoProductos

def cargar_grafo():
    grafo = GrafoProductos()
    productos = Producto.objects.all()

    for producto in productos:
        grafo.agregar_producto(producto.id)

    for producto in productos:
        relacionados = Producto.objects.filter(categoria=producto.categoria).exclude(id=producto.id)
        for r in relacionados:
            grafo.relacionar(producto.id, r.id)

    return grafo
