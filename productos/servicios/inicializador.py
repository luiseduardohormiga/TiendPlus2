from productos.estructuras.arbol import ArbolCategorias
from productos.models import Categoria

def inicializar_estructuras():
    arbol = ArbolCategorias()
    for c in Categoria.objects.all():
        arbol.insertar(c)
    return arbol
