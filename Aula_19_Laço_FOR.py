
'''
nome = 'Paulo'
for letra in nome:
    print(letra)
print("")
# Utilizando um contador
for n, letra in enumerate(nome):
    print(n,'====>' ,letra)
print("")
for n in range(10):
    print(n)
print(" ")
for n in range(0,10,2):
    print(n)
'''
print(" ")
texto = 'Python'
nova_string = ''

## Alterar a letra th para maiusculo TH
for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper() ##Será nova_string maiusculo.
    elif letra == 'h':
        nova_string += letra.upper() ##Será nova_string maiusculo.
    else:
        nova_string += letra
print(nova_string)














