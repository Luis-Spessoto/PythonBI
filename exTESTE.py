import pandas as pd  



tabelaFuncionarios = pd.read_excel('C:/Users/luisf/OneDrive/Área de Trabalho/pyhtonBI.24/Excel.Panda/tstExcelFuncionarios.xlsx')

salBase = float(input('Informe a faixa salarial que se deseja encontrar os fucionarios: '))

funciSALmaiorQUEbase = (tabelaFuncionarios.loc[tabelaFuncionarios['Salário'] >= salBase])
print(funciSALmaiorQUEbase)



import matplotlib.pyplot as plt

#histDADOS = tabelaFuncionarios[salBase].dropna() #df = DataFrame 

funciSALmaiorQUEbase.hist(column = 'Salário', bins = 100) #aqui ja utiliza os funciSALmaiorQUEbase pois ele ja e um subconjunto da tabela inicial
print(plt.show())