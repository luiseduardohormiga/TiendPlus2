from collections import deque, defaultdict

class GrafoProductos:
    def __init__(self):
        self.adj = defaultdict(list)  # key = producto_id, value = list de producto_id

    def agregar_producto(self, producto_id):
        _ = self.adj[producto_id]  # inicializa si no existe

    def relacionar(self, id1, id2, peso=1):
        if id2 not in [p for p,_ in self.adj[id1]]:
            self.adj[id1].append((id2, peso))
        if id1 not in [p for p,_ in self.adj[id2]]:
            self.adj[id2].append((id1, peso))

    def vecinos_directos(self, producto_id):
        return [pid for pid, _ in self.adj.get(producto_id, [])]

    def recomendar_nivel(self, producto_id, niveles=1):
        """
        Retorna recomendaciones hasta 'niveles' saltos.
        Por defecto niveles=1 => solo vecinos directos.
        """
        if producto_id not in self.adj:
            return []

        recomendados = []
        visited = set([producto_id])
        q = deque([(producto_id, 0)])
        while q:
            nodo, nivel = q.popleft()
            if nivel >= niveles: 
                continue
            for vecino, _ in self.adj[nodo]:
                if vecino not in visited:
                    visited.add(vecino)
                    recomendados.append((vecino, nivel+1))
                    q.append((vecino, nivel+1))
        # ordenamos por nivel (más cercanos primero)
        recomendados.sort(key=lambda x: x[1])
        return [pid for pid, _ in recomendados]