#Introdução à POO - Python

#Classes, Objetos. Métodos, Herança, Construtor

def teste (x, y):
    valor = x 
    incremeto = y
    resultado = x + y
    return resultado; 

x = int(input('X = '))
y= int(input('Y = '))
print(teste(x, y))

#CLasses  e Métodos 
#class e __init__
#classes são com iniciadas com letra maiuscula enquanto funcao (def) nao

class InstitutoTecmat:
    def incrementa(self, x, y): #self funciona como se fosse um ponteiro em linguagem C onde se trabalha com o endereco de um funcao e nao apenas seu valor (*valor e nao valor)
        valor = x
        incremento = y
        resultado = valor + incremento
        return resultado


#outra forma mais sofistica seria utilizando os enderecos/parametros (como ponteiros *)

class InstitutoTecmat:
    def incrementa(self, x, y): 
        self.valor = x
        self.incremento = y
        self.resultado = self.valor + self.incremento
        return self.resultado

    
a = InstitutoTecmat()
b = a.incrementa(10, 5)

print(b)
print(a.valor)

#metodo é uma função definida dentro de uma classe que opera sobre objetos dessa classe 

class InstitutoTecmat:
    def __init__ (self, x = 10, y = 1):
        self.valor = x
        self.incremento = y
        self.valorExponencial = x
    def incrementa(self):
        self.valor = self.valor + self.incremento 
    def verifica(self):
        if self.valor > 12:
            print("Ultrapassou 12")
        else: 
            print("Valor não ultrapassou 12")
    def exponencial(self, e):
        self.valorExponencial = self.valor**e
    def incrementaQuadrado(self):
        self.incrementa()
        self.exponencial(2)

a = InstitutoTecmat()
a.incrementa()
print(a.valor)
a.verifica()
a.exponencial(3)
print(a.valorExponencial)
a.incrementaQuadrado()
print(a.valor)

#Herança 

class Calc(InstitutoTecmat): #essa classe Calc vai utilizar todos os metodos e informacoes presentes na classe de dentro dos parenteses alem de suas proprias funcoes criadas
    def decrementa(self):
        self.valor= self.valor - self.incremento

c = Calc()
c.incrementa()
print(c.valor)

c = Calc()
c.decrementa()
print(c.valor)

class Calc(InstitutoTecmat):
    def __init__(self, d = 5): #__init__ é o metodo construtor utilizado para inializar os objetos de uma classe 
        super().__init__(x = 10, y = 1)
        self.divisor = d 
    def decrementa(self):
        self.valor = self.valor - self.incremento
    def divisao(self):
        self.valor = self.valor / self.divisor 

c = Calc()
c.divisao()
print(c.valor)