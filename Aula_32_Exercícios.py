
print('************** FUNÇÃO DO EXERCÍCIO 1 **************')
print()
cumprimento = str(input("Cumprimento: "))
nome = str(input("Nome: "))
print()
def saudacao(cumprimento, nome):
    print(cumprimento, nome)

saudacao(cumprimento, nome)
print()

print('************** FUNÇÃO DO EXERCÍCIO 2 **************')
print()
def som(a,b,c):
    soma = a + b + c
    return soma

resultado = som(1,2,3)
print(f'A soma destes números é {resultado}')

print('************** FUNÇÃO DO EXERCÍCIO 3 **************')
print()
a1 = int(input("Valor: "))
a2 = float(input("Percentual: "))

def fun(a1,a2):
    a2 = a2/100
    soma_2 = a1 + (a1*a2)
    return soma_2

result = fun(a1, a2)
print(result)
print()
print('************** FUNÇÃO DO EXERCÍCIO 4 **************')
print("Exercício do Fizz")
print()

def fizz(valor):
    if valor % 5 == 0 and valor % 3 == 0:
        return f'FizzBuzz: {valor} é divisível por 5 e por 3'
    if valor % 3 ==0 :
        return "Fizz: {valor} é divisível por 3"
    if valor % 5 == 0:
        return "Buzz: {valor} é divisível por 5"
    return valor
# Gerar números aleatórios entre 0 e 100
from random import randint
for i in range(100):
    aleatorio = randint(0,100)
    print(fizz(aleatorio))


print()
print('************** FUNÇÃO DO EXERCÍCIO 5 **************')
print()

def ola_mundo():
    return 'Olá mundo!'

def mestre(funcao): # Uma função recebe qualquer coisa como parâmetro (função, classe).
    return funcao()

executando = mestre(ola_mundo)
print(executando)

print()
print('************** FUNÇÃO DO EXERCÍCIO 6 **************')
print()

def mestre(funcao, *args, *kwargs):
    return funcao(*args, *kwargs)

def fala_oi(nome):
    return f'{oi} {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'Luis')
print(executando)























