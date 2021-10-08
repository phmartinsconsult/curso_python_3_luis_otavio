'''
O Python já identifica automaticamente o tipo da variável digitada
str - string - é um texto
int - inteiro - é um número inteiro
float - é um número flutuante
bool - boleano - é um valor que pode ser True or False
'''

print(12345,    "O tipo desta variável é", type(12345))

print('10',     "O tipo desta variável é", type('10'))

print(25.15,    "O tipo desta variável é", type(25.15))

print(10 == 10, "O tipo desta variável é", type(10==10))

print("Paulo" == "Vivi", "O tipo desta variável é", type("Paulo" == "Vivi"))

# TYPE CASTING - TROCAR O TIPO DA VARIAVEL
print("Paulo", type("Paulo"), bool("Paulo"))
# Quando nós colocamos o tipo da variável na frente dela
# o Python automaticamente toca o tipo da variável


paulo = "1000000"
paulo2 = 1000000
print(paulo, type(paulo)) # Perguntar o tipo da variável
print(paulo2, type(paulo2)) # Perguntar o tipo da variável
print(paulo2, str(paulo2)) # Alterar o tipo da variável
print(paulo, bool(paulo)) # Alterar o tipo da variável

print("")
# Exercícios
# String = nome
print("Paulo", type("Paulo"))

# Int = Idade
print(34, type(34))

# Float = Altura
print(1.60, type(1.60))

# Boll = maior de idade
print(34>18, type(34>18))























