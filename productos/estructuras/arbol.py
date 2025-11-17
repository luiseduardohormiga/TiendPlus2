# Arbol de categorías simple (orden lexicográfico). Usado solo en memoria para filtrar/mostrar.
class NodoArbol:
    def __init__(self, categoria):
        self.categoria = categoria
        self.izq = None
        self.der = None

class ArbolCategorias:
    def __init__(self):
        self.raiz = None

    def insertar(self, categoria):
        self.raiz = self._insertar(self.raiz, categoria)

    def _insertar(self, nodo, categoria):
        if nodo is None:
            return NodoArbol(categoria)
        if categoria.nombre < nodo.categoria.nombre:
            nodo.izq = self._insertar(nodo.izq, categoria)
        elif categoria.nombre > nodo.categoria.nombre:
            nodo.der = self._insertar(nodo.der, categoria)
        return nodo

    def inorder(self):
        res = []
        self._inorder(self.raiz, res)
        return res

    def _inorder(self, nodo, res):
        if nodo:
            self._inorder(nodo.izq, res)
            res.append(nodo.categoria)
            self._inorder(nodo.der, res)

    def buscar(self, nombre):
        return self._buscar(self.raiz, nombre)

    def _buscar(self, nodo, nombre):
        if nodo is None: return None
        if nodo.categoria.nombre == nombre:
            return nodo.categoria
        if nombre < nodo.categoria.nombre:
            return self._buscar(nodo.izq, nombre)
        return self._buscar(nodo.der, nombre)