from collections import deque

class GrafoProductos:
    def __init__(self):
        self.relaciones = {}

    def agregar_producto(self, producto_id):
        if producto_id not in self.relaciones:
            self.relaciones[producto_id] = []

    def relacionar(self, p1, p2):
        if p2 not in self.relaciones[p1]:
            self.relaciones[p1].append(p2)
        if p1 not in self.relaciones[p2]:
            self.relaciones[p2].append(p1)

    def recomendar_nivel(self, producto_id, niveles=1):
        visitado = set()
        cola = deque([(producto_id, 0)])
        visitado.add(producto_id)
        resultados = []

        while cola:
            nodo, nivel = cola.popleft()
            if nivel == niveles:
                resultados.append(nodo)
                continue
            for vecino in self.relaciones.get(nodo, []):
                if vecino not in visitado:
                    visitado.add(vecino)
                    cola.append((vecino, nivel + 1))

        return [r for r in resultados if r != producto_id]
