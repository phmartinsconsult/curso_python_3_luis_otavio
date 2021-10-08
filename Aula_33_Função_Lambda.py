'''
FUNÇÕES LAMBDA - ANÔNIMAS
'''

print('Uma função comum é assim:')
def funcao(arg, arg2):
    return arg * arg2
var = funcao(2,2)
print(var)
print()
print('Uma função lambda seria assim:')
a = lambda x,y : x*y
print(a(2,2))
# Usado quando quer passar essa função como parâmetro de outra função.
# Exemplo: Como ordernar os valores internos da lista?

lista = [
    ['Bombril', 13],
    ['Arroz', 7],
    ['Tomate', 9],
    ['Cebola', 15],
    ['Beterraba', 4]
]

# Poderia criar uma função normalmente:
#def func(item):
    #return item[1]

#lista.sort(key=func)
#lista.sort(key=func, reverse=True)
#print(lista)

# Ou poderia criar uma Função Anônima:
lista.sort(key=lambda item: item[1]) # repare que não tem vírgula.
lista.sort(key=lambda item: item[1], reverse=True) # repare que não tem vírgula.
lista.sort(key=lambda item: item[0]) # Ordernar pelo nome do produto P1
lista.sort(key=lambda item: item[0], reverse=True) # Ordem reversa.
print(lista)

# Ou poderia ser assim também:
print(sorted(lista, key=lambda i: i[1]))
print(sorted(lista, key=lambda i: i[1], reverse=True))
print(sorted(lista, key=lambda i: i[0])) # Ordenar pelo nome do produto P1
print(sorted(lista, key=lambda i: i[0], reverse=True))






















