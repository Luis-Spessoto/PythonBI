import time 
import math

#Bhaskara: (-b +- √b² - 4*a*c )/ 2 * a, para uma equação de segundo grau ax² + bx + c = 0

class Bhaskara:
    def dadosINPUT(self):
        print('A seguir, informe os valores de A, B e C, quando (ax² + bx + c = 0): ')
        a = float(input('Informe A: '))
        b = float(input('Informe B: '))
        c = float(input('Informe C: '))
        return a, b, c
    
    def processamento(self, a, b, c):
        delta = (b * b) - (4 * a * c)
        if delta < 0:   
            return delta, None, None #retorna None se delta negativo (None = vazio)
        else:
            x1 = (-(b) + math.sqrt(delta)) / (2 * a)
            x2 = (-(b) - math.sqrt(delta)) / (2 * a)
            return delta, x1, x2

    def respostas(self, a, b, c, delta, x1, x2):
        print(f'Para a equação: {a:.1f}x² + {b:.1f}x + {c:.1f} = 0,')
        print(f'Delta será igual a: {delta:.2f}')
        if x1 is None and x2 is None:
            print('Não existem raízes reais')
        else:
            print(f'E a equação quadrática terá como raìzes X1 = {x1:.2f} e X2 = {x2:.2f}')

def tudo():
    bhaskara = Bhaskara()
    a, b, c = bhaskara.dadosINPUT()
    delta, x1, x2 = bhaskara.processamento(a, b, c)
    bhaskara.respostas(a, b, c, delta, x1, x2)

tudo()
op = str(input('Quer continuar? [sim/não]: ')).upper()

while op != 'NAO' and op != 'NÃO':
    if op == 'SIM':
        tudo()
        op = str(input('Quer continuar? [sim/não]: ')).upper()        
    else:
        op = str(input("Opção Inválida! Tente novamente [sim/não]: ")).upper()

print('Encerrando processos...')
time.sleep(2)