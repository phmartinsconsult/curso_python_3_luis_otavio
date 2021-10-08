'''
Aula 2 - Classe, Objetos e Encapsulamento
'''


import math

# Criar uma classe
class Circ:

    def area(self, r):
        return math.pi*r*r

raio = int(input("Valor do Raio: "))
c1 = Circ() ## Classes e métodos sempre possuem parênteses
a = c1.area(raio)


print(f'O valor da área do raio do valor {raio} é {a}')