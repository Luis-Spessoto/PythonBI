'''
#print
print("Hello World!")

#tipos str, float, int
nome = str(input('Nome: ')).upper()
print(nome)
idade = int(input('Idade: '))
print(idade)
valor = float(input('Valor decimal: '))
print(valor)

#condicionais
if nome == 'LUIS':
    print("Seu nome é Luis")
elif nome == 'PEDRO':
    print("Seu nome é Pedro")
else:
    print('Seu nome não é nem Luis e nem Pedro')

'''
'''
#loop

#FOR
#for i in range():
#    print(i)

curso = 'python'

for i in curso:
    print(i)

qnt_filhos = int(input('Informe a quantidade de filhos: '))

for i in range(qnt_filhos):
    nomeFilho = str(input("Informe o nome do {}° filho: ".format(i + 1))) #para atribuir nome dos filhos a diferentes variaveis teria que criar uma lista e dar .append para adicionar

'''

''' 
uma forma de realizar o exemplo acima seria por meio de lista assim:
    
    qnt_filhos = int(input('Informe a quantidade de filhos: '))

    nomeFilhos = [] #isso aqui indica a criacao de uma lista para armazenar os nomes 

    for i in range(qnt_filhos):
        nomeFilho = str(input("Informe o nome do {}° filho: ".format(i + 1)))
        nomeFilhos.append(nomeFilho)

    for i in range(qnt_filhos): #esse seria um exemplo para a exibicao dos nomes da lista tipo Linguagem C
        print('Nome do {}° filho(a): {}'.format(i + 1, nomeFilhos[i]))    
'''
'''
#While

import time

contador = 0

while contador < 5:
    print('Vermelho')
    contador += 1 
    if contador == 3:
        break
    time.sleep(0.5)
print('Verde')

numeros = int(input('Informe um valor: '))
fatorial = numeros

i = 1
while (numeros - i) > 1:
    fatorial = fatorial * (numeros - i)
    i += 1

print('{}! = {}'.format(numeros, fatorial))

'''

#alguns modulos e bibliotecas

#import
# math
# time
# datetime

#funcoes, types e dados

# funcao = def

def apresentacao():
    print(' Ola \n Tudo bem? \n Eu sou Luis')

apresentacao()

def soma(a, b):
    resultado = a + b
    return resultado

n1 = int(input('N1: '))
n2 = int(input('N2: '))


result = soma(n1, n2)
print("{} + {} = {}".format(n1, n2, result))