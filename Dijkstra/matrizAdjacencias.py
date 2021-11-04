### Implementação de grafos representados por matriz de adjacências ###

class Grafo:

    def __init__(self, maximoVertices):
        self.vertices = maximoVertices
        self.matrizAdjacencias = [[0] * self.vertices for i in range(self.vertices)]
    
    def adicionarAresta(self, u, v, peso):
        self.matrizAdjacencias[u-1][v-1] = peso
        self.matrizAdjacencias[v-1][u-1] = peso
    
    def imprimirMatriz(self):
        for i in range(self.vertices):
            print(self.matrizAdjacencias[i])