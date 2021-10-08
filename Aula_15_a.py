'''
Faça um programa que peça o usuário para digitar um número inteiro,
informe se esse número é par ou impar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
'''
def par():
    print("")
    print('***************************************************')
    print('******* PROGRAMA VERIFICADOR DE INTEIROS **********')
    print('***************************************************')

    print(" ")

    numero_inteiro = input("Número inteiro: ")
    print("")
    if numero_inteiro.isdigit():
        numero_inteiro = int(numero_inteiro)
        if (numero_inteiro%2==0):
            print(f'{numero_inteiro} é par.')
        elif (numero_inteiro%2!=0):
            print(f'{numero_inteiro} é impar.')
    else:
        print("Esse número não é um inteiro.")
par()

