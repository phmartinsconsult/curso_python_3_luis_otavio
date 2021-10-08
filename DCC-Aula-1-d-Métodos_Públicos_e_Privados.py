'''
Encapsulamento - Ocultação de Classes
Podemos restringir o que pode ser acessado fora da Classe
Encapsulamento proporciona ABSTRAÇÕ - PROTEÇÃO
'''

import math
class Circ:

    def __init__(self, x=0.0, y=0.0, r=1.0):
        ########(self, x, y=0.0, r=1.0):
        self.x = x # atributos do método
        self.y = y
        self.r = r

    def __area(self): # Esse método é privado, ou seja, encapsulado: area é diferente de __area.
        #area(self):
        return math.pi*self.r*self.r

    def dist(self, circ): ## Esse é um método público
        return math.sqrt((self.x-circ.x)**2+(self.y-circ.y)**2)

    def __str__(self):
        return "Circunferência: " + str(self.x) + "," + str(self.y) + "," + str(self.r)

c1 = Circ()
#c1 = Circ(1.0)
a = c1.area()
print(a)

#c2 = Circ(5,0,5) ## Calculando a distância
#d = c2.dist(c1)
#print(d)


