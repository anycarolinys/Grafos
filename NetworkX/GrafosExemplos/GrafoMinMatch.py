# Grafo manual com arestas ponderadas também manualmente
''' Algoritmo do Problema de Atribuição Linear Retangular da biblioteca 
NetworkX: calcula o emparelhamento máximo com peso mínimo '''
import networkx as nx
import matplotlib.pyplot as plt

GrafoBipartido = nx.Graph()

GrafoBipartido = nx.Graph()


GrafoBipartido.add_nodes_from(["Cliente1", "Cliente2", "Cliente3", "Cliente4"], bipartite = 0)
GrafoBipartido.add_nodes_from(["Cliente5", "Cliente6", "Cliente7","Cliente8"], bipartite = 1)


GrafoBipartido.add_weighted_edges_from([('Cliente1','Cliente5',7), ('Cliente1','Cliente6',4), ('Cliente1','Cliente7',3), ('Cliente1','Cliente8',5)])
GrafoBipartido.add_weighted_edges_from([('Cliente2','Cliente5',6), ('Cliente2','Cliente6',8), ('Cliente2','Cliente7',5), ('Cliente2','Cliente8',9)])
GrafoBipartido.add_weighted_edges_from([('Cliente3','Cliente5',9), ('Cliente3','Cliente6',4), ('Cliente3','Cliente7',4), ('Cliente3','Cliente8',2)])
GrafoBipartido.add_weighted_edges_from([('Cliente4','Cliente5',3), ('Cliente4','Cliente6',8), ('Cliente4','Cliente7',7), ('Cliente4','Cliente8',4)])

match = nx.bipartite.minimum_weight_full_matching(GrafoBipartido)

GrafoResultante = nx.Graph()

print("Combinações")
for n in GrafoBipartido.nodes():
    GrafoResultante.add_edge(n, match[n], weight = GrafoBipartido[n][match[n]]['weight'])
    print(f"{n} - {match[n]}")
    print("Peso do match = ", end = ' ')
    print(GrafoBipartido[n][match[n]]['weight'])
    print()

print(GrafoResultante.edges())

plt.figure("Grafo Bipartido")
topo = ["Cliente1", "Cliente2", "Cliente3", "Cliente4"]
nx.draw_networkx(GrafoBipartido, pos = nx.bipartite_layout(GrafoBipartido, topo), with_labels = True)
nx.draw_networkx_edge_labels(GrafoBipartido, pos = nx.bipartite_layout(GrafoBipartido, topo))

plt.figure("Grafo Resultante")
nx.draw_networkx(GrafoResultante, pos = nx.bipartite_layout(GrafoResultante, topo), with_labels = True)
nx.draw_networkx_edge_labels(GrafoResultante, pos = nx.bipartite_layout(GrafoResultante, topo))
plt.show()