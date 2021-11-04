''' Uso da função que implementa o Algoritmo de Correspondência com Peso Mínimo (Problema de 
atribuição linear retangular) do NetworkX '''

import networkx as nx

GrafoBipartido = nx.Graph()

GrafoBipartido.add_nodes_from(['a','b','c','d'], bipartite = 0)

GrafoBipartido.add_nodes_from(['e','f','g','h'], bipartite = 1)

print(GrafoBipartido.nodes())

GrafoBipartido.add_weighted_edges_from([('a','e',7), ('a','f',4), ('a','g',3), ('a','h',5)])
GrafoBipartido.add_weighted_edges_from([('b','e',6), ('b','f',8), ('b','g',5), ('b','h',9)])
GrafoBipartido.add_weighted_edges_from([('c','e',9), ('c','f',4), ('c','g',4), ('c','h',2)])
GrafoBipartido.add_weighted_edges_from([('d','e',3), ('d','f',8), ('d','g',7), ('d','h',4)])


dicionarioMatch = nx.bipartite.minimum_weight_full_matching(GrafoBipartido)

print(dicionarioMatch)