import random
import numpy as np
import matplotlib.pyplot as plt

uniforme = []
gaussiana = []

''' for i in range(100):
    # valor = random.randint(0,10) # Gerando valores aleatórios inteiros entre 0 e 10
    valor = random.random() # Gerando valores aleatórios reais entre 0 e 1
    valoresAleatorios.append(valor) '''
    
# Distribuição uniforme
# Esse tipo de distribuição denota que os valores são distribuídos uniformemente, é possível visualizar melhor esse tipo de distribuição exibindo em um histograma
for i in range(1000):
    valor = random.uniform(1000, 3000)
    uniforme.append(valor)
    # Primeiro parâmetro média
    # Segundo parâmetro desvio padrão
    valor = random.gauss(0, 1)
    gaussiana.append(valor)
    
# plt.plot(uniforme)
plt.plot(gaussiana)
plt.show()

""" sample1 = np.random.uniform(3000,10000,100)
print(sample1)

sample2 = np.random.gauss(10000, 5)
print(sample2) """
""" count, bins, ignored = plt.hist(sample, 15, density = True)
plt.plot(bins, np.ones_like(bins), linewidth = 2, color = 'r')
plt.show() """