import pandas as pd   

tabela = pd.read_csv('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/RandomFiles/archive/tst.csv')
print(tabela.head(4))

print(tabela.shape)

tabela2 = tabela.dropna() #elimina toda informacao inexistente NaN
print(tabela2.head(4))

print(tabela2.shape)

dadosNulosNAN = tabela.isnull() #verfica se dados sao nulos ou nao True/False
print(dadosNulosNAN.head(4))

NaN = tabela.isnull().sum() #.sum informa a quantidade de itens requiridos
print(NaN)

tabela['Medal'].fillna('Zero', inplace = True) #nisso aqui o fillna subistui no campo medalhas quando nao tiver (NaN) por Zero
print(tabela.head(4))

