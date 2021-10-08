'''
Entrada dos dados - Função INPUT
'''

'''
nome = input("Digite o seu nome: ")
print("")
print(f'O usuário digitou o seguinte {nome}',
      f'e essa variável é do tipo {type(nome)}')
'''

print('******************************')
print('*** CALCULADORA PROGRAMADA ***')
print('******************************')
print(" ")
print("Se for soma, digite 1")
print("Se for subtração, digite 2")
print("Se for multiplicação, digite 3")
print("Se for divisão, digite 4")
print("")
form = int(input("Qual a função da calculadora você quer usar? "))
print("")
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
if form == 1:
      print("O resultado da soma é: ", a + b)
elif form == 2:
      print("O resultado da subtração é:", a - b)
elif form == 3:
      print("O resultado da multiplicação é: ", a * b)
elif form == 4:
      print("O resultado da divisão é: ", a/b)















