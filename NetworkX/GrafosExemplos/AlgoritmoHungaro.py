# Geração de grafo bipartido aleatório com peso nas arestas pseudoaleatório #
# ALgoritmo húngaro: retorna o emparelhamento maximal com peso máximo nas arestas #
import random
import queue
import networkx as nx
import matplotlib.pyplot as plt

visitado = []
caminho = []

def novoEmparelhamento(match, t):
    global caminho
    
    while True:
        x = caminho[t]
        match[t] = x
        match[x] = t
        t = caminho[x]
        if (t == x):
            break

def esvaziarFila(fila):
    with fila.mutex:
        fila.queue.clear()

def aumentarEmparelhamento(GrafoBipartido: nx.Graph(), cor, match):
    global visitado
    global caminho

    visitado = [False for i in range(GrafoBipartido.number_of_nodes())]
    caminho = [0 for i in range(GrafoBipartido.number_of_nodes())]
    
    fila = queue.Queue()

    # Adicionando todos os vertices solteiros 
    # de cor 0 à fila
    for vertice in GrafoBipartido.nodes():
        if cor[vertice] == 0 and match[vertice] == -1:
            visitado[vertice] = True
            caminho[vertice] = vertice
            fila.put(vertice)
    
    while not(fila.empty()):
        vertice = fila.get()

        for adj in GrafoBipartido[vertice]:
            if not(visitado[adj]):
                visitado[adj] = True
                caminho[adj] = vertice
                if match[adj] == -1:
                    novoEmparelhamento(match, adj)
                    esvaziarFila(fila)
                    return True
                x = match[adj]
                visitado[x] = True
                caminho[x] = adj
                fila.put(x)

    esvaziarFila(fila)
    return False

def algoritmoHungaro(GrafoBipartido: nx.Graph(), cor, match):
    tamanhoEmparelhamento = 0

    while (aumentarEmparelhamento(GrafoBipartido, cor, match)):
        tamanhoEmparelhamento += 1

    return tamanhoEmparelhamento

GrafoBipartido = nx.algorithms.bipartite.generators.gnmk_random_graph(4,4,9)
for aresta in GrafoBipartido.edges():
    v1 = aresta[0]
    v2 = aresta[1]
    GrafoBipartido[v1][v2]['weight'] = random.randint(50, 100)

cor = []

for n in GrafoBipartido.nodes():
    cor.append(GrafoBipartido.nodes[n]['bipartite'])

match = [-1 for i in range(GrafoBipartido.number_of_nodes())]

emparelhamento = algoritmoHungaro(GrafoBipartido, cor, match)

print(f"TAMANHO DO EMPARELHAMENTO = {emparelhamento}")
print()


GrafoResultante = nx.Graph()

print("MATCHES")
for n in GrafoBipartido.nodes():
    print(f"{n} - {match[n]}")
    if match[n] != -1:
        GrafoResultante.add_edge(n, match[n])
        GrafoResultante[n][match[n]]['weight'] = GrafoBipartido[n][match[n]]['weight']
        ''' print("Peso do match = ", end = ' ')
        print(GrafoBipartido[n][match[n]]['weight'])
        print() '''

plt.figure("Grafo Bipartido")
topo = [0,1,2,3]
nx.draw_networkx(GrafoBipartido, pos = nx.bipartite_layout(GrafoBipartido, topo), with_labels=True)
nx.draw_networkx_edge_labels(GrafoBipartido, pos = nx.bipartite_layout(GrafoBipartido, topo))

plt.figure("Grafo Resultante")
topo = [0,1,2,3]
nx.draw_networkx(GrafoResultante, pos = nx.bipartite_layout(GrafoResultante, topo), with_labels=True)
nx.draw_networkx_edge_labels(GrafoResultante, pos = nx.bipartite_layout(GrafoResultante, topo))
plt.show()