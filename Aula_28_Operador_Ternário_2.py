'''
Operadores Ternários em Python
'''


idade = input("Idade: ")

if not idade.isnumeric():
    print("Você precisa digitar apenas números!")
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    print()
    msg = 'Pode acessar!' if e_de_maior else 'Não pode acessar!' ## Esses são os operadores ternários.

    print(msg)


