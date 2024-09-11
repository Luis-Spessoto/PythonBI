import matplotlib.pyplot as plt
import pandas as pd

#matplotlib é utilizado para criar gráficos utilizando python

tabela = pd.read_csv('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/RandomFiles/archive/tst.csv')
'''tabela.hist(column = 'Height', bins = 10) #hist = grafico histograma o  bins se refere a "resolucao" das informacoes 
print(plt.show()) #esse aqui mostra como fica'''

tabela.boxplot(column='Age')
plt.show()
tabela.hist(column='Age', bins = 100)
plt.show()
