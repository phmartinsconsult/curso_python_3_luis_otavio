'''
Exercício
'''

import sys
from Classes import *
case = int(sys.stdin.readline())


class Ponto2D:

    def __init__(self, x=0.0, y=0.0):
        self.x = x # atributos do método
        self.y = y

class Retangulo:
    """
    Parametros do Retangulo1
    """
    r1_se_x, r1_se_y, r1_id_x, r1_id_y = list(map(float, sys.stdin.readline().split()))
    r1_esq_sup = Ponto2D(r1_se_x, r1_se_y)
    r1_dir_inf = Ponto2D(r1_id_x, r1_id_y)
    ret1 = Retangulo(r1_esq_sup, r1_dir_inf)

    """
    Parametros do Retangulo2
    """
    r2_se_x, r2_se_y, r2_id_x, r2_id_y = list(map(float, sys.stdin.readline().split()))
    r2_esq_sup = Ponto2D(r2_se_x, r2_se_y)
    r2_dir_inf = Ponto2D(r2_id_x, r2_id_y)
    ret2 = Retangulo(r2_esq_sup, r2_dir_inf)

    def __init__(self, esq_sup, dir_inf):
        __self.esq_sup = Ponto2D.x  # atributos do método
        __self.dir_inf = Ponto2D.y

    if case == 0:
        area1 = ret1.calcularArea()
        print("%.2f %.2f %.2f" % (ret1.width, ret1.height, area1))
    elif case == 1:
        area2 = ret2.calcularArea()
        print("%.2f %.2f %.2f" % (ret2.width, ret2.height, area2))
    elif case == 2:
        """
        Verificando intersercao
        """
        intersecao = ret1.calcularIntersecao(ret2)
        if intersecao == None:
            print(intersecao)
        else:
            print("%.2f" % intersecao)


r1_esq_sup = Ponto2D(-6.5, 5.0)
print(r1_esq_sup)
r1_dir_inf = Ponto2D(-2.0, 2.5)
ret1 = Retangulo(r1_esq_sup, r1_dir_inf)
area1 = ret1.calcularArea()
print("%.2f %.2f %.2f" % (ret1.width, ret1.height, area1))

r2_esq_sup = Ponto2D(2.0, 7.0)
r2_dir_inf = Ponto2D(5.0, 4.0)
ret2 = Retangulo(r2_esq_sup, r2_dir_inf)
area2 = ret2.calcularArea()
print("%.2f %.2f %.2f" % (ret2.width, ret2.height, area2))
intersecao = ret1.calcularIntersecao(ret2)
print(intersecao)


'''

c1 = Circ()
#c1 = Circ(1.0)
a = c1.area()
print(a)

#c2 = Circ(5,0,5) ## Calculando a distância
#d = c2.dist(c1)
#print(d)
'''

