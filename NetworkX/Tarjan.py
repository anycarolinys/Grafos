# Algoritmo de Tarjan
# Este algoritmo é implmentando pelo método 'nx.strongly_connected_components' da biblioteca Networkx
# Referência: https://www.ime.usp.br/~pf/algoritmos_para_grafos/aulas/tarjan.html
import networkx as nx
import matplotlib.pyplot as plt
from Stack import Stack

numPreOrdem = 0
cc = 0
pre = []
stack = Stack()


def componentesFortes(Grafo):
    global pre
    pre = [-1 for i in range(Grafo.number_of_nodes())]
    componentes = [-1 for i in range(Grafo.number_of_nodes())]
    low = [-1 for i in range(Grafo.number_of_nodes())]

    numComponente = 0
    
    for n in Grafo.nodes():
        if pre[n] == -1:
            buscaProfundaComponente(Grafo, n, componentes, low)
    
    return (numComponente, componentes)


def buscaProfundaComponente(Grafo, vertice, componentes, low):
    global pre
    global numPreOrdem
    global stack
    global cc
    
    pre[vertice] = numPreOrdem
    numPreOrdem += 1
    
    stack.append(vertice)
    low[vertice] = pre[vertice]
    
    for adj in Grafo[vertice]:
        
        if pre[adj] == -1:
            buscaProfundaComponente(Grafo, adj, componentes, low)
            low[vertice] = min(low[vertice], low[adj])
        
        elif pre[adj] < pre[vertice] and componentes[adj] == -1:
            low[vertice] = min(low[vertice], pre[adj])
    
    if low[vertice] == pre[vertice]:
        
        u = stack.pop()
        componentes[u] = cc
        while u != vertice:
            u = stack.pop()
            componentes[u] = cc
        cc += 1

def drawGraph(graph):

    position2 = nx.spring_layout(graph, k=0.5, seed = 42)
    nx.draw_networkx(graph,
                    position2,
                    with_labels = True,
                    node_size = 400,
                    node_color = "mistyrose",
                    edge_cmap = plt.cm.Blues_r,
                    style = "solid",
                    width = 1)

# GrafoDirigido = nx.gaussian_random_partition_graph(500, 50, 10, 0.5, 0.2, True)

GrafoDirigido = nx.DiGraph()

GrafoDirigido.add_edges_from(([0,1], [0,5], [2,0], [2,3], [3,2], [3,5], [4,2], [4,3], [5,4], [6,0], [6,4], [6,9], [7,6], [7,8], [8,7], [8,9], [9,10], [9,11], [10,12], [11,4], [11,12], [12,9]))

numComponente, vetorComponentes = componentesFortes(GrafoDirigido)

conjuntoComponentes = [[] for i in range(len(vetorComponentes))]
selecionada = []

for n in GrafoDirigido.nodes():
        if (vetorComponentes[n] not in selecionada):
            print("Componente = %d" % (vetorComponentes[n]))
            for i in range(n, GrafoDirigido.number_of_nodes()):
                if (vetorComponentes[n] == vetorComponentes[i]):
                    conjuntoComponentes[vetorComponentes[n]].append(i)
                    print("Vertice %d" % (i))
            selecionada.append(vetorComponentes[n])

print(conjuntoComponentes)

Componentes = nx.DiGraph()

for vetorComponentes in conjuntoComponentes:
    if len(vetorComponentes) == 1:
        Componentes.add_node(vetorComponentes[0])
    for vertice in vetorComponentes:
            for n in GrafoDirigido.neighbors(vertice) :
                if n in vetorComponentes:
                    Componentes.add_edges_from([(vertice, n)])
    if Componentes.number_of_nodes() > 0:
        plt.figure("Grafo Original")
        drawGraph(GrafoDirigido)
        plt.figure("Componente")
        drawGraph(Componentes)
        plt.show()
        Componentes.clear()


''' Teste do método nativo

print([
    len(c)
    for c in sorted(nx.strongly_connected_components(GrafoDirigido), key=len, reverse=True)
])

for c in nx.strongly_connected_components(GrafoDirigido):
    print("Tamanho = %d" % len(c))
    for v in c:
        print(v)

print(len(list(nx.strongly_connected_components(GrafoDirigido)))) '''