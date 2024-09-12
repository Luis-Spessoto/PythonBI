import pandas as pd 

tabelaFuncionarios = pd.read_excel('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/Excel.Panda/tstExcelFuncionarios.xlsx')
print(tabelaFuncionarios)

print(tabelaFuncionarios.describe()) #descreve contagem, media, min, porcentagens, max e desvio padrao
print('\n')
print(tabelaFuncionarios['Salário'].max()) #encontra o maior salario apenas 
print('\n')

funciMAIS50 = (tabelaFuncionarios.loc[tabelaFuncionarios['Data de Nascimento'] <= '1974'])
print(funciMAIS50) 

funciSALmaiorQUEmedia = (tabelaFuncionarios.loc[tabelaFuncionarios['Salário'] >= 5492.00])
print(funciSALmaiorQUEmedia)

QNTfunciSALmaiorQUEmedia = (tabelaFuncionarios['Salário'] >= 5492.00).sum() #conta apenas quantas pessoas sao
print('\n ', QNTfunciSALmaiorQUEmedia)


#esses 2 de baixo funcionam igual para retirar o campo/coluna Teste da tabela
#tabelaSemTESTE = tabelaFuncionarios.drop(columns=['Teste'])
#tabelaSemTESTE = tabelaFuncionarios.drop('Teste', axis=1)
#print(tabelaSemTESTE)

import matplotlib.pyplot as plt

tabelaFuncionarios.hist(column = 'Salário', bins = 100)
print(plt.show())
