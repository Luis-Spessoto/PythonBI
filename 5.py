import pandas as pd 

tabela_Olympics = pd.read_csv('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/RandomFiles/archive/tst.csv')
print(tabela_Olympics.head())

'''#print(tabela_Olympics.rename(columns={'Name': 'Nome', 'Sex': 'Sexo', 'Age': 'Idade', 'Sport' : 'Esporte'})) #para alterar infos]
tabela_Olympics.rename(columns={'Name': 'Nome', 'Sex': 'Sexo', 'Age': 'Idade', 'Sport' : 'Esporte'}, inplace = True) #para alterar infos e o inplace salva informacoes dos lugares alterados
print(tabela_Olympics.head())

print(tabela_Olympics['Idade'][0:5])'''

#drop é para retirar/eliminar

tabela_Olympics.drop('ID', axis = 1, inplace=True) #eliminou o id das pessoas
print(tabela_Olympics.head())

tabela_Olympics.drop('Age', axis = 1, inplace=True) #elimina a idade
print(tabela_Olympics.head())