'''
OPERADORES LÓGICOS OR - Economizam tempo e linhas de código
'''


a = 0
b = []
c = {}
d = False
e = 22
f = 'Luis'

variavel = (a or b or c or d or f) ## Ele vai imprimir o valor correto
print(variavel)
# print(a or b or c or d or f))
'''
Melhor do que fazer assim:
if a:
    variavel = a
elif b:
    variavel = b
elif c:
    variavel = c
....
'''