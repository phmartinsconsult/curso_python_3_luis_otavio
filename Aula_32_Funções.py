
print("FUNÇÃO 1")
print()
def calcula(a, b=10):
    if a == 0:
        divide = a / b
    else:
        divide = a / b
    print(f'O resultado da sua soma é {divide}')

'''
if divide:
    print(divide)
else:
    print('Conta invalida')
'''

som = calcula(0)

print('FUNÇÃO 2')
print()
def funcao(var):
    return var

var = funcao('Valor que eu quero')
print(var)

def divisao(n1,n2):
    if n2 == 0:
        return
    return n1/n2

divide_1 = divisao(8,2)

if divide_1:
    print(divide_1)
else:
    print('Conta inválida')

print(type(divide_1))

print('FUNÇÃO 3')
print('#######################################')
print()
def f(var):
    print(var)

def dumb():
    return f
var = dumb()
print(f'O tipo dessa variável é: {type(var)}.') ## Classe Function
print(f'O id dessas variáveis é: a: {id(var)} e b: {id(f)}')

print('FUNÇÃO 4')
print()

def dumb():
    return ("Luis","Otávio")

dum = dumb()




