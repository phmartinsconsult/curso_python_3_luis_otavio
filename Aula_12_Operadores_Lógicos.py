'''
Operadores Lógicos - AND, OR, NOT
* (Verdadeiro and Verdadeiro) = Verdadeiro ## As duas precisam ser verdadeiros.
* (Verdadeiro or Falso) = Falso ## Pelo menos, uma precisa ser verdadeira.
* NOT = Inverte o sinal
* IN e NOT IN
'''

nome = str(input("Digite o seu nome: "))
a = input("Digite o valor de a: ")
b = input("Digite o valor de b: ")
print(" ")
'''
if not a:
    print("Preencha o valor de a, por favor")
elif not b:
    print("Preencha o valor de b, por favor.")
elif not a and b:
    print("Preencha os valores de a e b, por favor.")
else:
    print("Deu tudo certo!")
'''
if "a" in a:
    print(f'{nome}, sua resposta foi correta.')
else:
    print(f'{nome} Sua resposta não está correta.')


