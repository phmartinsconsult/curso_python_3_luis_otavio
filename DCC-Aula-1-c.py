
import math

class Circ:

    def __init__(self, x=0.0, y=0.0, r=1.0):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return math.pi*self.r*self.r

    def __str__(self):
        return "Circunferência: " + str(self.x) + "," + str(self.y) + "," + str(self.r)


c1 = Circ()
print()
print(c1) # Vai imprimir os valores já definidos antes
