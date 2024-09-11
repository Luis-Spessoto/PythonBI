import pandas as pd

notas = {'Alunos': ['Bruno', 'João', 'Ana', 'Jose'], 
         'Notas': ['10', '7', '10', '4'],
         'Situação': ['Aprovado', 'Aprovado', 'Aprovado', 'Reprovado']}

tabelDADOS = pd.DataFrame(notas)
print(tabelDADOS)

#pd.Series = criar um array unidimensional (vetor) 
pares = pd.Series([2,4,6,8])
print(pares)

import numpy as np

impares = np.array([1,3,5,7])
print(impares)

primos = np.array([(2,3,5,7), (11,13,17,19)])
print(primos)

#diferenca entre numpy e pandas é que nujmpy so trabalha com numeros enquanto o pandas tambem trabalha com strings

'''sequencia = pd.Series(primos)
print(sequencia)''' #nao funciona pq o array primos é bidimensional 

notas = {'Alunos': ['Bruno', 'João', 'Ana', 'Jose'], 
         'Notas': ['10', '7', '10', '4'],
         'Situação': ['Aprovado', 'Aprovado', 'Aprovado', 'Reprovado']}

tabelDADOS = pd.DataFrame(notas)
print(tabelDADOS)

print(tabelDADOS.shape) #estrutura da tabela
print('\n{}'.format(tabelDADOS.describe())) #breve descricao da tabela
print(tabelDADOS['Situação']) #informa apenas a coluna Situação (a qual é requerida)
print(tabelDADOS.loc[1]) #loc serve para localizar informacoes ou linhas especificas, nesse caso linhas 
print(tabelDADOS.loc[[1,2,3]]) #ou print(tabelDADOS.loc[1:3])
print(tabelDADOS.loc[tabelDADOS['Notas'] == '10']) #para localizar as informacoes referentes quando as notas sao igual a 10
print(tabelDADOS.loc[tabelDADOS['Situação'] == 'Aprovado']) #info quando Aprovado
#df tambem pode ser utilizado para encontrar informacoes so que ele encontra direto ao DataFrame ou arquivo enquanto o Loc encontra por rotulo (nome dado)
