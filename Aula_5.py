'''
Operadores Aritméticos
'''


print('Multiplicação utiliza * : ', 10 * 10)
print("Divisão utiliza a barra / : ", 10/10)
print('Adição utiliza o + : ', 10 + 10)
print('Subitração utiliza o - :', 10 - 10)
print('Multiplicação utiliza o * : ', 10 * '10')
print("")
print("")
print("")
# Concatenação com operadores aritméticos

def fun_operadores():
    a = str(input("Insira o primeiro número: " ))
    b = str(input("Insira o segundo número: " ))
    c = int(input("Insira um número inteiro: " ))
    barra = input("Insira um operador lógico: ")
    print("")
    print("Os números concatenados são ", a + b)
    print("Vamos mostrar a união das informações e os operadores lógicos", a + barra + b)
    print("Vamos unir os seguintes argumentos: ", a + str(c))
fun_operadores()

# Não podemos unir inteiro com string
print("")
print("Vamos fazer alguns cálculos de exemplos:")
print(10/3)
print(10//3) # Retorna apenas o inteiro, mesmo que esteja flutuante.
print(10**3)
print(10%3) # Esse é o módulo e retorna o resto da divisão.

