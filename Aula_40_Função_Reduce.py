'''
FUNÇÃO REDUCE - FUNÇÃO ACUMULADORA
'''

from dados import pessoas, produtos, lista
from functools import reduce

# Podemos trabalhar de duas maneiras:
# List Comprehension e For
acumula = 0
for item in lista:
    acumula+=item
print(f'Utilizando o For, a soma dos valores da lista é {acumula}.')

soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(f'Utilizando o reduce, a soma dos valores da lista é {soma_lista}.')

soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(f'A média das idades dessas pessoas é: {soma_idades/len(pessoas)}')








