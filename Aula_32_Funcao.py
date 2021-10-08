
print('FUNÇÃO 1')
print('')
def fun(a1, a2, a3=None):
    print(a1,a2,a3)
    print(f'Os valores da função são: {a1}, {a2}, {a3}')
    return (a1,a2)

var = fun(1,2,a3='Paulo')
print(var[0], var[1]) #Está retornando o valor de RETURN

print()
print('FUNÇÃO 2')
print('')
def argum(*args):
    print(args)

lista = [1,2,3,4,5]
n1, n2,*n = lista
# Observe o args
# Estamos empacotando o *n com os valores
# Args é um empacotamento também
print(n1, n2, n)

