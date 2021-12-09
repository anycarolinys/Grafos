import random
import networkx as nx
import matplotlib.pyplot as plt
# Gerando um grafo de partição aleatória gaussiana
# Quantidade de nós = 50
# Tamanho médio do cluster = 10
# Parâmetro de forma (variação do tamanho da distribuição do cluster é a média dividida por este valor) = 10
# Probabilidade de conexão dos nós dentro dos clusters = 100%
# Probabilidade de conexão dos nós entre os clusters = 50%
# Grafo direcionado = sim

GrafoNormal = nx.gaussian_random_partition_graph(25, 10, 10, 0.1, 0.1, True)

# Gerando um grafo binomial
# Quantidade de nós = 50
# Probabilidade da criação de arestas = 50%
# GrafoBinomial = nx.generators.random_graphs.binomial_graph(50, 0.50)

sampleWeights = []
for i in range(GrafoNormal.number_of_edges()):
    # w = random.uniform(50000, 100000)
    w = random.gauss(100000, 10000)
    sampleWeights.append(w)

for e,w in zip(GrafoNormal.edges(), sampleWeights):
    v1 = e[0]
    v2 = e[1]
    GrafoNormal[v1][v2]['weight'] = int(w)

for e in GrafoNormal.edges():
    v1 = e[0]
    v2 = e[1]
    print(f"{v1} - {v2} = ", end = '')
    print(GrafoNormal[v1][v2]['weight'])

plt.figure("Grafo")
nx.draw_networkx(GrafoNormal, pos= nx.spring_layout(GrafoNormal), with_labels=True)
nx.draw_networkx_edge_labels(GrafoNormal, pos = nx.spring_layout(GrafoNormal))
plt.show()