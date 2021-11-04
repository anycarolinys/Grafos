### Implementação de grafos representados por listas de adjacências ###

class Grafo:
    def __init__(self, maximoVertices):
        self.vertices = maximoVertices
        self.listaAdjacencias = [[] for i in range(maximoVertices)]

    def adicionarAresta(self, origem, destino, peso):
        self.listaAdjacencias[origem-1].append([destino, peso])
        self.listaAdjacencias[destino-1].append([origem, peso])

    def imprimirLista(self):
        for i in range(self.vertices):
            print(f'{i+1}:', end = "  ") # 'end' adicionado para impedir a quebra de linha
            for j in self.listaAdjacencias[i]: #iterando sobre a lista, não é necessário 'range'
                print(f"{j} ->", end = "  ")
            print("\n")