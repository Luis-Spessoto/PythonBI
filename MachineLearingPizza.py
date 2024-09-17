#Projeto Machine Learning - Preço Pizza baseado no Diâmetro


#importação de bibliotecas 
import numpy as np #manipulat vetores (arrays)
import matplotlib.pyplot as plt #para visualizar dados - grafico
from sklearn.linear_model import LinearRegression #para criar modelo de regressao linear
from sklearn.metrics import mean_squared_error, r2_score #para avaliar o modelo


#Crirar  um  conjunto de dados ficticios com o diametro e o preco de algumas pizzas
x = np.array([6, 8, 10, 14, 18]) #diametro em polegadas das pizzas
y = np.array([7, 9, 13, 17.5, 18]) #preço em reais das pizzas


#Visualizar os dados em um grafico de dispersao
plt.scatter(x, y) #criar grafico do diametro pelo preco
plt.xlabel('Diâmetro em polegadas') #nomeia 
plt.ylabel('Preço em Reais') #nomeia
plt.title('Preço da Pizza em razão de seu diâmetro') #adicionar titulo do grafico
plt.show() #mostrar o grafico construitdo


#Criar e treinar um modelo de regressão linear com dados
model = LinearRegression() #instanciar o modelo
x = x.reshape(-1, 1) #transformar o array X em uma matriz de uma coluna
model.fit(x, y) #treinar o modelo com os dados informados no array 


#Avaliar o desempenho do modelo com algumas métricas
y_pred = model.predict(x) #fazer as previsôes para os dados de treino
mse = mean_squared_error(y, y_pred) #calcular o erro quadrático médio [soma de todos os resultados tidos como erros em relação à previsão inicial e, posteriormente devidi-los pela quantidade de valores somados]
r2 = r2_score(y, y_pred) #calcular o coeficiente de determinação (r2) [medida de ajuste de um modelo estatistico linear, o r2 pode variar entre 0 e 1]
print(f'{mse:.2f}') #para 2 casas decimais :.2f
print(r2)


#Fazer uma previsão para uma nova pizza
xNOVO = np.array([12]) #diametro da nova pizza
yNOVO = model.predict(xNOVO.reshape(-1, 1))
print(f'Uma pizza de {xNOVO} polegadas custaria {yNOVO} reais')
