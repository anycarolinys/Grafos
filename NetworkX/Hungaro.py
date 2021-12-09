''' Implementação do Algoritmo Húngaro para encontrar um emparelhamento máximo em um grafo não-dirigido 
para grafos representados usando a biblioteca NetworkX '''

import networkx as nx
import queue

visitado = []
caminho = []

def esvaziarFila(fila):
    with fila.mutex:
        fila.queue.clear()

def novoEmparelhamento(match, t):
    global caminho

    x = caminho[t]

    while t != x:
        x = caminho[t]
        match[t] = x
        match[x] = t
        t = caminho[x]

def aumentarEmparelhamento(Grafo: nx.Graph(), coloracao, match):
    global visitado
    global caminho
    visitado = [False for i in range(Grafo.number_of_nodes())]
    caminho = [0 for i in range(Grafo.number_of_nodes())]

    fila = queue.Queue()

    for no in Grafo.nodes():
        if coloracao[no] == 0 and match[no] == -1:
            visitado[no] = True
            caminho[no] = no
            fila.put(no)
    # A fila contém todos os vértices solteiros (sem match) de cor 0

    while not(fila.empty()):
        vertice = fila.get()
        print(vertice)

        for adj in Grafo[vertice]:
            if not(visitado[adj]):
                visitado[adj] = True
                caminho[adj] = vertice
                if (match[adj] == -1):
                    novoEmparelhamento(match, adj)
                    esvaziarFila(fila)
                    return True
            seg = match[adj]
            visitado[seg] = True
            caminho[seg] = adj
            fila.put(seg)
    esvaziarFila(fila)
    return False

def MetodoHungaro(Grafo: nx.Graph(), coloracao, match):
    # match = [-1 for i in range(Grafo.number_of_nodes())]

    tamanhoEmparelhamento = 0
    while aumentarEmparelhamento(Grafo, coloracao, match) == True:
        tamanhoEmparelhamento += 1
    return tamanhoEmparelhamento

GrafoBipartido = nx.Graph()

GrafoBipartido.add_nodes_from(['a','b','c','d'], bipartite = 0)

GrafoBipartido.add_nodes_from(['e','f','g','h'], bipartite = 1)

GrafoBipartido.add_weighted_edges_from([('a','e',7), 
('a','f',4), 
('a','g',3), 
('a','h',5)])
GrafoBipartido.add_weighted_edges_from([('b','e',6), 
('b','f',8), 
('b','g',5), 
('b','h',9)])
GrafoBipartido.add_weighted_edges_from([('c','e',9), 
('c','f',4), 
('c','g',4), 
('c','h',2)])
GrafoBipartido.add_weighted_edges_from([('d','e',3), 
('d','f',8), 
('d','g',7), 
('d','h',4)])


GrafoInteiro = nx.convert_node_labels_to_integers(GrafoBipartido)

match = [-1 for i in range(GrafoInteiro.number_of_nodes())]
coloracao = [-1 for i in range(GrafoInteiro.number_of_nodes())]

for n in GrafoInteiro.nodes():
    coloracao[n] = GrafoInteiro.nodes[n]['bipartite']

tamanho = MetodoHungaro(GrafoInteiro, coloracao, match)

print(tamanho)
print(match)

emparelhamento = 0

for i in range(GrafoInteiro.number_of_nodes()):
    m = match[i]
    print(f"Vertice: {i}, match: {m}")
    print(GrafoInteiro[i][m]['weight'])