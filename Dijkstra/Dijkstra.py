### Implementação do algoritmo de Dijkstra para grafos representados por matriz de adjacências ###

import heapq as mininumHeap
from matrizAdjacencias import Grafo

def Dijkstra(grafo: Grafo, origem):
    custoPartida = [[-1,0] for i in range(grafo.vertices)]

    custoPartida[origem - 1] = [0, origem]

    heap = []

    mininumHeap.heappush(heap, [0, origem])

    while len(heap) > 0:
        distancia, vertice = mininumHeap.heappop(heap)
        
        for i in range(grafo.vertices):
            if grafo.matrizAdjacencias[vertice - 1][i] != 0:
                if custoPartida[i][0] == -1 or custoPartida[i][0] > distancia + grafo.matrizAdjacencias[vertice - 1][i]:
                    custoPartida[i] = [distancia + grafo.matrizAdjacencias[vertice - 1][i], vertice]
                    mininumHeap.heappush(heap, [distancia + grafo.matrizAdjacencias[vertice-1][i], i+1])
    return custoPartida