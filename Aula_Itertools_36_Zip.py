'''
ZIP - Unindo iteráveis
zip_longest = itertools
'''

from itertools import zip_longest

cidades = ['São Paulo', 'Belo Horizonte', 'Porto Alegre', 'Monte Belo']

estados = ['SP', 'MG','RS']

cidades_estados = zip(estados, cidades)
#print(list(cidades_estados))
#print(dict(cidades_estados))
#lc = (print(valor) for valor in cidades_estados)
#print(lc)
#print(cidades_estados)
for valor in cidades_estados:
    print(valor)

cidades_estados = zip_longest(estados, cidades)
print(list(cidades_estados))


lista_a = [1,2,3,4,5,6,7,8]
lista_b = [3,4,5,6]
lista_soma = []
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i]+lista_b[i])
print(lista_soma)

# Solução Pythônica = Decorar
lista_somada = [x+y for x,y in zip(lista_a,lista_b)]
print(lista_somada)






















