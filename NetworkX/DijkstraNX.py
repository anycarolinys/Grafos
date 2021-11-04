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

        print(f"distancia: {distancia}, vertice: {vertice}")

        for adj in grafo[vertice]:
            if custoPartida[adj][0] == -1 or custoPartida[adj][0] > distancia + grafo[vertice][adj]['weight']:
                custoPartida[adj] = [distancia + grafo[vertice][adj]['weight'], vertice]
                mininumHeap.heappush(heap, [distancia + grafo[vertice][adj]['weight'], adj])

    return custoPartida

Grafo = nx.DiGraph()

Grafo.add_nodes_from(["Construtora"], preco = 1000)
Grafo.add_nodes_from(["Cliente1"], preco = 2000)
Grafo.add_nodes_from(["Cliente2"], preco = 3000)
Grafo.add_nodes_from(["Cliente3"], preco = 4000)
Grafo.add_nodes_from(["Cliente4"], preco = 5000)
Grafo.add_nodes_from(["Cliente5"], preco = 6000)
Grafo.add_nodes_from(["Cliente6"], preco = 7000)

Grafo.add_edge('Construtora','Cliente1', weight = 10)
Grafo.add_edge('Cliente1','Cliente6', weight = 21)
Grafo.add_edge('Cliente1','Cliente2', weight = 1)
Grafo.add_edge('Cliente2','Cliente4', weight = 3)
Grafo.add_edge('Cliente3','Cliente1', weight = 4)
Grafo.add_edge('Cliente4','Cliente3', weight = 10)
Grafo.add_edge('Cliente4','Cliente6', weight = 26)
Grafo.add_edge('Cliente4','Cliente5', weight = 22)


GrafoInteiro = nx.convert_node_labels_to_integers(Grafo)

resultado = Dijkstra(GrafoInteiro, 0)


print(resultado)