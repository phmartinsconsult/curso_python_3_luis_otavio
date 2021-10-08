print()
print("Função 1")
print()
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))
d = int(input("Digite o valor de d: "))

def mat(a,b,c,d):
    calc = a + b * c / d
    print(f'O resultado deste calculo é: {calc}')

mat(a,b,c,d)
print()
print("**************************************")
print("Função Concatenar")
print()
def concat(a,b, c='Viegas', d='Martins'):
    concatenar = a + " " + b + " " + c + " " + d
    print(f'O resultado desta concatenação é: {concatenar}')

concat('Paulo', 'Henrique')
concat("Paulo", "Henrique", c="Carvalho")
print()
print("Outra Função")
def replace(a,b):
    a = a.replace("p","c")
    b = b.replace("g", "h")
    return a + " "+ b

replace = replace("Paulo","Henrique")
print(replace)
print('******************************************')
print("Função Condicional")
def cond(alfa, beta):
    if alfa == 0:
        return alfa/beta
    return alfa/beta

cond = cond(0,8)
print(cond)

print('Classe Função')
print()

def f(var):
    print(var)

def dumb():
    return f

var = dumb()
print(f'Afunção de var é : {type(var)}')
















