import networkx as nx
import matplotlib.pyplot as plt
import random

# Desenhando o grafo completo com peso nas arestas
def drawGraph(graph, density = False):
    # Extraindo as arestas e os pesos
    edges, weights = zip(*nx.get_edge_attributes(graph, 'weight').items()) 
    pos = nx.spring_layout(graph, k=0.05, seed = 42)
    nx.draw_networkx(graph,
                    pos,
                    with_labels = True,
                    node_size = 400,
                    node_color = "mistyrose",
                    edgelist = edges,
                    edge_color = weights,
                    edge_cmap = plt.cm.Blues_r,
                    style = "solid",
                    width = 1)
    
    # plt.subplots_adjust(left = 2, bottom = 3.2, right = 6, top = 6)
    
    if density:
        print("----------------------------------------")
        print("Density:",nx.classes.function.density(graph))
        print("----------------------------------------")
    
    return plt.show()

# Analisando um nó específico no grafo
def drawNodeGraph(graph, nodename, info = False, weightbar = 0):
    # 'graph' é o grafo original
    # 'nodename' é o nome do nó a ser analisado
    # o valor padrão para 'weightbar' é 0, se aumentar a barra, a relação rara será removida. Assumindo que não há pesos negativos
    
    # Copia os grafos mas os atributos são compartilhados com o grafo original
    temp = graph.copy(as_view = False)
    
    #Remove a relação rara entre arestas se o 'weightbar' não for 0
    temp.remove_edges_from((e for e, w in nx.get_edge_attributes(temp, 'weight').items() if w <= weightbar))
    
    # Gera lista com os nós que possuem relacionamento com o nó alvo
    nodelist = list(temp.neighbors(n = nodename))
    # Insere o nó alvo na lista de nós
    nodelist.append(nodename)
    
    # Gerando subgrafo com a lista de nós
    Subgraph = temp.subgraph(nodelist)
    
    edges, weights = zip(*nx.get_edge_attributes(Subgraph, 'weight').items())
    
    pos = nx.spring_layout(Subgraph, k = 0.7, seed = 42)
    
    node_map = {nodename: 7000}
    
    # Aumentar o nó alvo
    nodesize = [node_map.get(node, 3500) for node in Subgraph.nodes()]
    
    val_map = {nodename:0.5714285714285714}
    
    # Mudar a cor do nó alvo
    nodecolor = [val_map.get(node, 0.25) for node in Subgraph.nodes()]
    
    # Mudar a largura da aresta com base nos pesos das arestas
    width = [w * 5 for w in weights]
    
    nx.draw_networkx(Subgraph,
                    pos,
                    cmap = plt.get_cmap('viridis'),
                    with_labels = True,
                    node_size = nodesize,
                    node_color = nodecolor,
                    edge_cmap = plt.cm.Blues_r,
                    style = "solid",
                    font_color = "white",
                    font_size = 20,
                    width = width)
    # plt.subplots_adjust(left = 2, bottom = 3.2, right = 6, top = 6)
    
    if info:
        print("----------------------------------------")
        print("Density:",nx.classes.function.density(Sub))
        print("The information of the graph:",nx.info(Sub))
        print("----------------------------------------")
        
    return plt.show()

GrafoNormal = nx.gaussian_random_partition_graph(25, 10, 10, 0.1, 0.1, True)

sampleWeights = []
for i in range(GrafoNormal.number_of_edges()):
    w = random.gauss(100000, 10000)
    sampleWeights.append(w)

for e,w in zip(GrafoNormal.edges(), sampleWeights):
    v1 = e[0]
    v2 = e[1]
    GrafoNormal[v1][v2]['weight'] = int(w)
    # GrafoNormal.add_weighted_edges_from(([v1, v2, int(w)]))

drawGraph(GrafoNormal)
drawNodeGraph(GrafoNormal, 10)