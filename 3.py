#Pandas = manipulacao de tabelas 
import pandas as pd

#ler tabela pronta excel = xlsx
tabela = pd.read_excel('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/Excel.Panda/Excel.1.xlsx')

#para escrever a tabela lida
print(tabela.head())
print('\n')
print(tabela.head(6))

#para ler csv = _csv
tabela_Olympics = pd.read_csv('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/RandomFiles/archive/tst.csv')
print(tabela_Olympics.head(5))