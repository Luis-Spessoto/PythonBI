#Projeto Machine Learning 

#arquivo sobre vinhos tintos ou brancos (0/1)

import pandas as pd  
import matplotlib.pyplot as plt 

arquivo = pd.read_csv('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/RandomFiles/archive/wine_dataset.csv')
print(arquivo.head())

'''
contRED = (arquivo['style'] == 'red').sum()
contBRA = (arquivo['style'] == 'white').sum()
print(contRED)
print(contBRA)
'''

#trocando a cor dos vinhos por 0 e 1
arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)

print(arquivo.head())

#separando as variaveis
y = arquivo['style']
x = arquivo.drop('style', axis = 1)

print(y)
print(arquivo.head())

#criando treino e teste pra maquina entender a saber qual e tinto e qual e branco (0/1)

from sklearn.model_selection import train_test_split 
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size = 0.3)

print(x_teste.shape)

from sklearn.ensemble import ExtraTreesClassifier

#criando o modelo
modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

#imprimindo o resultado
resultado = modelo.score(x_teste, y_teste)
print('Probabilidade: ', resultado)


print(y_teste[500:505])
print(x_teste[500:505])