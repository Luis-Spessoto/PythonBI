def soma(a, b):
    return a + b
def menos(a, b):
    return a - b
def mult(a, b):
    return a * b
def divi(a, b):
    return a / b

n1 = int(input('N1: '))
n2 = int(input('N2: '))
print("Escolha uma operação: ")
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Sair')
op = int(input('Informe o número da operação [1/2/3/4/5]: '))

r1 = soma(n1, n2)
r2 = menos(n1, n2)
r3 = mult(n1, n2)
r4 = divi(n1, n2)

while op != 5:
    if op == 1: 
        print('{} + {} = {}'.format(n1, n2, r1))
    elif op == 2:
        print('{} - {} = {}'.format(n1, n2, r2))
    elif op == 3:
        print('{} * {} = {}'.format(n1, n2, r3))
    elif op == 4:
        print('{} / {} = {:.2f}'.format(n1, n2, r4))
    else:
        break
    op2 = str(input('Quer continuar? Sim ou não? ')).upper()
    if op2 == 'SIM':
        n1 = int(input('N1: '))
        n2 = int(input('N2: '))
        print("Escolha uma operação: ")
        print('1 - Adição')
        print('2 - Subtração')
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Sair')
        op = int(input('Informe o número da operação [1/2/3/4/5]: '))
    else: 
        break