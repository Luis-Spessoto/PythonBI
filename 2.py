'''
#listas e append 

n1 = int(input('Informe a quantidade de itens para a lista de compras: '))
lista = []

for i in range(n1):
    itemLista = str(input('Informe o {}° item: '.format(i + 1)))
    lista.append(itemLista) #append adiciona item à lista

for i in range(n1):
    print('{}° item da lista: {}'.format((i + 1), lista[i]))

#Choice = funcao importada da biblioteca random

import random

cores = ['azul', 'vermelho', 'amarelo']
sorteado = random.choice(cores)
print("A cor escolhida aleatorimente é: {}".format(sorteado))

#Tuplas = imutavel

lista = [1, 3, 5, 7]
type(lista)


Tupla = (2, 4, 6, 8)
type(Tupla)

tupla2 = tuple(lista)
print(tupla2)

#Dicionarios = primeiro chave : segundo valor

dicio = {'refrigerante':'r$ 5,00', 
         'suco' : '10,00',
         'Agua': '2,50'}

print(dicio['refrigerante'])

print(dicio.values())
print(dicio.keys())
print(dicio.items())


#Manipulação de Strings

apresentacao = 'Eu nasci em 1990 e moro em São Paulo'

print(apresentacao[0:16])
print(apresentacao[0:16:2])
print(apresentacao.count('e'))
print(len(apresentacao))
print(apresentacao.replace('em São Paulo', 'no Brasil'))


#Função Lambda e funções anônimas

def mult(x, y):
    multi = x * y
    return multi

mult(5, 2)

multi2 = lambda x, y: x * y
multi2(2, 5)


#Função Map e List Comprehension
#diferentes formas de se manipular uma lista

polegadas = [1, 2, 3, 4, 5, 6, 7, 8]

mm = []

#1
for i in polegadas:
    mm.append(i*25.4)
print(mm)

#2
mm2 = list(map(lambda x: x * 25.4, polegadas))
print(mm2)

#3
mm3 = [x * 25.4 for x in polegadas]
print(mm3)

'''

