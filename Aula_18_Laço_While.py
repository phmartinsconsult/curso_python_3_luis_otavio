'''
Objetivo: Laço de Repetição While e DEBUGAR o Código
'''

'''
x = 0
while x < 5:
    print(x)
    x = x + 1
    continue # ou break

print("Acabou")
'''
## Função Calculadora
def calc():
    while True:
        print()
        num_1 = input("Digite o primeiro número: ")
        num_2 = input("Digite o segundo número: ")
        operador = input("Digite o operador: ")

        if not num_1.isnumeric() or not num_2.isnumeric():   ## Verificar se é numérico
            print("Você precisa digitar o número novamente.")
            continue

        num_1 = int(num_1)
        num_2 = int(num_2)

        # + - / x
        if operador == "+":
            print("")
            print("Resultado: ", num_1 + num_2)
        elif operador == "-":
            print("")
            print("Resultado: ", num_1 - num_2)
        elif operador == '/':
            print("")
            print("Resultado: ", num_1/num_2)
        elif operador == 'x':
            print("")
            print("Resultado: ", num_1 * num_2)
calc()











