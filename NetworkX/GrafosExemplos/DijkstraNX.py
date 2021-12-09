### Implementação do algoritmo de Dijkstra para grafos representados usando a biblioteca NetworkX ###

import networkx as nx
import heapq as mininumHeap
import numpy as np

def Dijkstra(grafo: nx.DiGraph(), origem):
    custoPartida = [[-1,0] for i in range(grafo.number_of_nodes())]
    custoPartida[origem] = [0, origem]

    heap = []

    mininumHeap.heappush(heap, [0, origem])

    while len(heap) > 0:
        distancia, vertice = mininumHeap.heappop(heap)  

        # print(f"distancia: {distancia}, vertice: {vertice}")

        for adj in grafo[vertice]:
            if custoPartida[adj][0] == -1 or custoPartida[adj][0] > distancia + grafo[vertice][adj]['peso']:
                custoPartida[adj] = [distancia + grafo[vertice][adj]['peso'], vertice]
                mininumHeap.heappush(heap, [distancia + grafo[vertice][adj]['peso'], adj])

    return custoPartida