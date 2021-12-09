import random
import networkx as nx
import matplotlib.pyplot as plt
# from DijkstraNX import Dijkstra
import heapq as mininumHeap

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

Grafo = nx.generators.directed.gn_graph(25)

pesos = []

for e in Grafo.edges():
    w = int(random.gauss(100000, 50000))
    v1 = e[0]
    v2 = e[1]
    Grafo[v1][v2]['weight'] = w

plt.figure("Grafo de Rede Crescente")
nx.draw_networkx(Grafo, pos = nx.planar_layout(Grafo))
nx.draw_networkx_edge_labels(Grafo, pos = nx.planar_layout(Grafo))

lista = list(Grafo.nodes)
resultado = Dijkstra(Grafo, 0)

print("VETOR RESULTANTE")
print(resultado)
print()

GrafoResultante = nx.DiGraph()

print('PROPOSTAS')
for i in range(Grafo.number_of_nodes()):
    if lista[i] != lista[resultado[i][1]]:
        GrafoResultante.add_edge(lista[resultado[i][1]], lista[i])
        print(f"VENDE: {lista[resultado[i][1]]}", end=' --- ')
        print(f"COMPRA: {lista[i]}")

plt.figure("Grafo Resultante")
nx.draw_networkx(GrafoResultante, pos = nx.planar_layout(GrafoResultante))
nx.draw_networkx_edge_labels(GrafoResultante, pos = nx.planar_layout(GrafoResultante))
plt.show()

GrafoKOut = nx.generators.directed.random_k_out_graph(25, 2, 2, False)

""" plt.figure("Grafo K Out")
nx.draw_networkx(GrafoKOut, pos = nx.spring_layout(GrafoKOut))
nx.draw_networkx_edge_labels(GrafoKOut, pos = nx.spring_layout(GrafoKOut)) """