# Componentes Conexas para Grafos não dirigidos
import networkx as nx
import matplotlib.pyplot as plt

numComponentes = 0

def componentesConexas(Grafo):
    vetorComponentes = [-1 for i in range(Grafo.number_of_nodes())]
    
    global numComponentes
    
    for n in Grafo.nodes():
        if(vetorComponentes[n] == -1):
            buscaProfundidade(Grafo, n, vetorComponentes, numComponentes)
            numComponentes += 1
            
    return numComponentes, vetorComponentes


def buscaProfundidade(Grafo, vertice, vetorComponentes, componente):
    vetorComponentes[vertice] = componente
    
    for adjacente in Grafo[vertice]:
        
        if(vetorComponentes[adjacente] == -1):
            buscaProfundidade(Grafo, adjacente, vetorComponentes, componente)


def drawGraph(graph, density = False):
    pos = nx.spring_layout(graph, k=0.05, seed = 42)
    nx.draw_networkx(graph,
                    pos,
                    with_labels = True,
                    node_size = 400,
                    node_color = "mistyrose",
                    edge_cmap = plt.cm.Blues_r,
                    style = "solid",
                    width = 1)


# Gerando um grafo de partição aleatória gaussiana
# Quantidade de nós = 500
# Tamanho médio do cluster = 50
# Parâmetro de forma (variação do tamanho da distribuição do cluster é a média dividida por este valor) = 10
# Probabilidade de conexão dos nós dentro dos clusters = 0.5%
# Probabilidade de conexão dos nós entre os clusters = 0.2%
# Grafo direcionado = não

GrafoNormal = nx.gaussian_random_partition_graph(500, 50, 10, 0.005, 0.002)

qtdComponentes, componente = componentesConexas(GrafoNormal)

Componentes = nx.Graph()

conjuntoComponentes = [[] for i in range(len(componente))]

selecionada = []

for n in GrafoNormal.nodes():
        if (componente[n] not in selecionada):
            for i in range(n, GrafoNormal.number_of_nodes()):
                if componente[i] == componente[n]:
                    conjuntoComponentes[componente[n]].append(i)
            selecionada.append(componente[n]) 

print("Conjunto de componentes: ")
print(conjuntoComponentes)

for componente in conjuntoComponentes:
    if len(componente) == 1:
        Componentes.add_node(componente[0])
    for vertice in componente:
            for n in GrafoNormal.neighbors(vertice):
                Componentes.add_edges_from([(vertice, n)])
    if Componentes.number_of_nodes() > 0:
        plt.figure("Grafo Original")
        drawGraph(GrafoNormal)
        plt.figure("Componente")
        drawGraph(Componentes)
        plt.show()
        Componentes.clear()

""" selecionada = []

for n in GrafoNormal.nodes():
        if (componente[n] not in selecionada):
            print("Componente = %d" % (componente[n]))
            for i in range(n, GrafoNormal.number_of_nodes()):
                if (componente[n] == componente[i]):
                    print("Vertice %d" % (i))
            selecionada.append(componente[n]) """