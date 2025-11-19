class NodoCategoria:
    def __init__(self, categoria):
        self.categoria = categoria
        self.izquierda = None
        self.derecha = None


class ArbolCategorias:
    def __init__(self):
        self.raiz = None

    def insertar(self, categoria):
        nuevo = NodoCategoria(categoria)

        if not self.raiz:
            self.raiz = nuevo
            return

        actual = self.raiz
        while True:
            if categoria.nombre < actual.categoria.nombre:
                if actual.izquierda is None:
                    actual.izquierda = nuevo
                    return
                actual = actual.izquierda
            else:
                if actual.derecha is None:
                    actual.derecha = nuevo
                    return
                actual = actual.derecha

    def ordenar(self):
        resultado = []

        def inorden(nodo):
            if nodo:
                inorden(nodo.izquierda)
                resultado.append(nodo.categoria)
                inorden(nodo.derecha)

        inorden(self.raiz)
        return resultado