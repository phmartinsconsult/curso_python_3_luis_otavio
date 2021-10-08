
import math
print()
print('*******************************')
print('****** CRIAÇÃO DA CLASSE ******')
print('*******************************')
print()

class Circ:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return math.pi*self.r*self.r

x = int(input("Valor de x: "))
y = int(input("Valor de y: "))
r = int(input("Valor de r: "))

c1 = Circ(x, y, r) # Estou instanciando a classe
a = c1.area()
print()
print(f'A área calculada é: {a:.2f}')

