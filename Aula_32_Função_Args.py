print('**************** ARGS E KWARGS ****************')

def fun_args(*args):
    print(args)

lista = [1,2,3,4,5,6,7,8,9] #Imagine que aqui tenha uma coluna de uma tabela.
fun_args(*lista)


print('**************** FUNÇÃO 1 ****************')
print('')
# Essa função aqui retorna uma Tupla
def argum(*args):
    print(args)
    print(f'O primeiro argumento dessa lista é: {args[0]}')
    print(f'O último argumento desta lista é: {args[-1]}') # F String
    print(f'O tamanho desta lista é {len(args)}')

argum(1,2,3,4,5) # Chamar a função

print('FUNÇÃO 2')
print('')
# Essa função aqui retorna uma Tupla
def argum(*args):
    args = list(args)
    args[0] = 20 # Setamos o valor [0]
    print(args)
    print(f'O primeiro argumento dessa lista é: {args[0]}')
    print(f'O último argumento desta lista é: {args[-1]}') # F String
    print(f'O tamanho desta lista é {len(args)}')
    print(f'O maior valor dessa lista é {max(args)}')

argum(1,2,3,4,5) # Chamar a função

print('FUNÇÃO 3')
print('')
# Essa função aqui retorna uma Tupla
def argum(*args):
    args = list(args)
    args[0] = 20 # Setamos o valor [0]
    for v in args:
        print(args)
        print(f'O primeiro argumento dessa lista é: {args[0]}')
        print(f'O último argumento desta lista é: {args[-1]}') # F String
        print(f'O tamanho desta lista é {len(args)}')
        print(f'O maior valor dessa lista é {max(args)}')

argum(1,2,3,4,5) # Chamar a função

print('********* FUNÇÃO 4 *********')
print('')
def argum(*args):
    print(args)

lista1 = [1,2,3,4,5,6,7]
lista2 = [8,9,10,11]


argum(*lista1, *lista2) # Chamar a função
argum(lista1, lista2)


print('********* FUNÇÃO 5 *********')
lista = [1,2,3,4,5]
print(*lista) ## Enpacotamos todos os valores da lista