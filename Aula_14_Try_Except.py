'''
TRY AND EXCEPT
'''

print('******************************')
print('*** CALCULADORA PROGRAMADA ***')
print('******************************')

# Não deixar o usuário caminhar se não digitar números corretamente.
num1 = input("Primeiro número: ")
num2 = input("Segundo número: ")
try:  ## Tenta fazer isso.
      num1 = int(num1)
      num2 = int(num2)
      print("")
      print("O resultado é", num1+num2,".")

except: ## Se não der certo, faça isso!
      print("")
      print("Não pode converter os números para fazer cálculos")