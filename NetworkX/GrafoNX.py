### Explorando as funcionalidades da biblioteca NetworkX ###

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
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

''' Grafo['Construtora']['Cliente1']['peso'] = 10
Grafo['Cliente1']['Cliente6']['peso'] = 21
Grafo['Cliente1']['Cliente2']['peso'] = 1
Grafo['Cliente2']['Cliente4']['peso'] = 3
Grafo['Cliente3']['Cliente1']['peso'] = 4
Grafo['Cliente4']['Cliente3']['peso'] = 10
Grafo['Cliente4']['Cliente6']['peso'] = 26
Grafo['Cliente4']['Cliente5']['peso'] = 22 '''

print("Lista de vértices")
print(Grafo.nodes())

print("Percorrendo os vértices")
for v in Grafo.nodes():
    print(v, end = "-> ")
    print(Grafo.nodes[v]['preco']) 

NovoGrafo = nx.convert_node_labels_to_integers(Grafo)

print("Nova lista de vértices")
print(NovoGrafo.nodes()) 

print("Lista de arestas")
print(Grafo.edges()) 

print("Percorrendo as arestas")
for e in Grafo.edges():
    print(e)

print("Sequência de graus do grafo")
print(Grafo.degree()) 

print("Acessando grau do vértice individualmente")
for n in Grafo.nodes():
    print("Vértice", end=' \'')
    print(n, end = "\', grau: ")
    print(Grafo.degree()[n]) 

print("Lista de adjacência de cada vértice")
for n in Grafo.nodes():
    print("Vértice", end=' \'')
    print(n, end = "\', lista: ")
    for adj in Grafo[n]:
        print(adj, end=" ->")
    print('\n')

print("Matriz de adjacências de G")
M = nx.to_numpy_matrix(Grafo)
print(M)

# Adicionando peso nas arestas
for e in Grafo.edges():
    v1 = e[0]
    v2 = e[1]
    Grafo[v1][v2]['peso'] = Grafo.nodes[v2]['preco'] - Grafo.nodes[v1]['preco']

print("Peso das arestas")
for e in Grafo.edges():
    v1 = e[0]
    v2 = e[1]
    print(f'{v1} - {v2} = ', end='')
    print(Grafo[v1][v2]['weight'])

GrafoInteiro = nx.convert_node_labels_to_integers(Grafo)

plt.figure("Grafo")
nx.draw_networkx(Grafo, pos= nx.spring_layout(Grafo), with_labels=True)
nx.draw_networkx_edge_labels(Grafo, pos = nx.planar_layout(Grafo))
plt.show()