# Grafo manual com arestas ponderadas por operações realizadas nos atributos dos nós #
''' Algoritmo de Dijkstra: retorna o menor caminho entre o nó de origem e todos os
nós alcançáveis por ele '''
import networkx as nx
import matplotlib.pyplot as plt
from DijkstraNX import Dijkstra

Grafo = nx.DiGraph()

Grafo.add_nodes_from(["Construtora"], compra = -1, venda = 100000)
Grafo.add_nodes_from(["Cliente1"], compra = 70000, venda = 50000)
Grafo.add_nodes_from(["Cliente2"], compra = 80000, venda = 50000)
Grafo.add_nodes_from(["Cliente3"], compra = 40000, venda = 75000)
Grafo.add_nodes_from(["Cliente4"], compra = 60000, venda = 60000)
Grafo.add_nodes_from(["Cliente5"], compra = 40000, venda = -1)

Grafo.add_edge("Construtora", "Cliente1")
Grafo.add_edge("Construtora", "Cliente2")
Grafo.add_edge("Construtora", "Cliente3")
Grafo.add_edge("Cliente1", "Cliente5")
Grafo.add_edge("Cliente2", "Cliente3")
Grafo.add_edge("Cliente3", "Cliente4")
Grafo.add_edge("Cliente3", "Cliente5")
Grafo.add_edge("Cliente4", "Cliente5")

# Definindo peso nas arestas
for aresta in Grafo.edges():
    v1 = aresta[0]
    v2 = aresta[1]
    Grafo[v1][v2]['peso'] = Grafo.nodes[v1]['venda'] - Grafo.nodes[v2]['compra']

lista = list(Grafo.nodes)

GrafoInteiro = nx.convert_node_labels_to_integers(Grafo)

resultado = Dijkstra(GrafoInteiro, 0)

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

plt.figure("Grafo Original")
nx.draw_networkx(Grafo, pos=nx.planar_layout(Grafo), with_labels=True)
nx.draw_networkx_edge_labels(Grafo, pos=nx.planar_layout(Grafo))

plt.figure("Grafo Resultante")
nx.draw_networkx(GrafoResultante, pos = nx.planar_layout(GrafoResultante), with_labels = True)
nx.draw_networkx_edge_labels(GrafoResultante, pos = nx.planar_layout(GrafoResultante))
plt.show()