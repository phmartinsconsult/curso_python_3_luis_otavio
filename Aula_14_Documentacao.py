'''
Funções:
string.isnumeric()
string.isdigit()
'''

print('******************************')
print('*** CALCULADORA PROGRAMADA ***')
print('******************************')

# Não deixar o usuário caminhar se não digitar números corretamente.
num1 = input("Primeiro número: ")
num2 = input("Segundo número: ")
if num1.isdigit() and num2.isdigit():
      num1 = int(num1)
      num2 = int(num2)
      print("")
      print("O resultado é", num1+num2,".")

else:
      ("Não pode converter os números para fazer cálculos")