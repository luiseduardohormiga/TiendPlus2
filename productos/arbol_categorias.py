# ARCHIVO: productos/arbol_categorias.py

class NodoCategoria:
    def __init__(self, categoria):
        self.categoria = categoria
        self.hijos = []

class ArbolCategorias:
    def __init__(self):
        self.raiz = NodoCategoria(None)

    def insertar(self, categoria):
        if categoria.padre is None:
            self.raiz.hijos.append(NodoCategoria(categoria))
        else:
            padre_nodo = self.buscar_nodo(self.raiz, categoria.padre)
            if padre_nodo:
                padre_nodo.hijos.append(NodoCategoria(categoria))

    def buscar_nodo(self, nodo_actual, categoria_objetivo):
        if nodo_actual.categoria == categoria_objetivo:
            return nodo_actual
        for hijo in nodo_actual.hijos:
            resultado = self.buscar_nodo(hijo, categoria_objetivo)
            if resultado:
                return resultado
        return None

    def ordenar(self):
        resultado = []
        self._ordenar_recursivo(self.raiz, resultado)
        return resultado

    def _ordenar_recursivo(self, nodo, resultado):
        for hijo in nodo.hijos:
            resultado.append(hijo.categoria)
            self._ordenar_recursivo(hijo, resultado)
