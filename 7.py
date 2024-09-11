import matplotlib.pyplot as plt  

valor = [2,4,6,8,10,12,14,16]
produto = [1,2,3,4,5,6,7,8]

plt.scatter(valor, produto) #primeiro seria x (coluna) e o segundo y (linha)
plt.show()

import numpy as np

x = np.arange(0, 100, 1) #cria um range/limite de valores nesse caso comeca em 0 vai ate 99 num passo de 1 em 1 (99 pq do 0 ate 99 sao 100 numeros)
print(x)

plt.plot(x, x**2)
plt.show()