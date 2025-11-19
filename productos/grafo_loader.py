from .models import Producto
from .grafo import GrafoProductos

def cargar_grafo():
    grafo = GrafoProductos()

    # Cargar nodos
    for p in Producto.objects.all():
        grafo.agregar_producto(p.id)

    # --------------------------
    # REGLAS DE RELACIÓN
    # --------------------------

    for p in Producto.objects.all():

        # 1. Relación por categoría
        mismos = Producto.objects.filter(categoria=p.categoria).exclude(id=p.id)
        for r in mismos:
            grafo.relacionar(p.id, r.id, peso=1)

        # 2. Relación por precio cercano (+/- 10)
        cercanos = Producto.objects.filter(
            precio__gte=p.precio - 10,
            precio__lte=p.precio + 10
        ).exclude(id=p.id)
        for r in cercanos:
            grafo.relacionar(p.id, r.id, peso=2)

        # Aquí puedes añadir más reglas si quieres

    return grafo