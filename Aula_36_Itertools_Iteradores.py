'''
ITERADORES
'''

lista = [1,2,3,4,5]
print(hasattr(lista, '__iter__')) # Verificar se essa é uma lista ITERÁVEL.

# ITERADOR: gerar um valor de cada vez.
# Como é um ITERÁVEL, podemos criar um LOOPE FOR.
# O loope FOR transforma a variável em um ITERADOR.
# Note que a lista é um iterável, porém não é um ITERADOR.
print(hasattr(lista, '__next__')) # Verificar se essa é um ITERADOR.

for i in lista: # O for transformou a lista em um iterador.
    print(i)

lista = iter(lista) #Cast para transformar em um iterador.

print('#' *80)
# GERADORES: Utilizados quando precisamos utilizar muita memória
import sys
import time
























