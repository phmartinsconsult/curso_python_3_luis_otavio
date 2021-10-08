'''
LIST COMPREHENSION
OBJETIVOS - OTIMIZAÇÃO E REDUZIR QUANTIDADE DE CÓDIGOS
'''

l1 = [1,2,3,4,5]
ex1 = [v for v in l1] # Apenas repetiu os mesmos números # Implicitamente há um PRINT
print(ex1)
print('')
ex2 = [v*2 for v in l1] #Multiplicar cada número por dois
print(ex2)
print('')
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex3)
print('')
l2 = ['Paulo', 'Eduardo', 'Patrícia']
ex4 = [v.replace('a', '@') for v in l2]
print(ex4)
print('')
ex5 = [v.replace('a', '@').upper() for v in l2]
print(ex5)
print('')
ex6 = [v.replace('a', '@').endswith('G') for v in l2]
print(ex6)
print('')
tupla = (
    ('chave','valor'),
    ('chave1','valor1')
)
ex7 = [(y, x) for x,y in tupla] # Inverter o valor dentro das tuplas
print(ex7)
print('')
l3 = range(50)
ex8 = [v for v in l3 if v % 2 == 0]
ex9 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(ex8)
print(ex9)
ex10 = [v if v % 3 == 0 else 'Não é par' for v in l3]
print(ex10)
ex11 = [v if v % 3 == 0 else 0 for v in l3]
print('')
ex12 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex12)































