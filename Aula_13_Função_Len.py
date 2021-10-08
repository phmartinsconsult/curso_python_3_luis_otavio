'''
A função LEN
'''

usuario = input("Digite seu usuário: ")
qtd_usuario = len(usuario)
print("")

if qtd_usuario < 6:

    print("Você deve inserir um usuário com, pelo menos, 6 dígitos.")

else:

    print("Usuário correto. Você foi cadastrado no sistema.")


