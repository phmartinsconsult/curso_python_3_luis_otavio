'''
DEBUGAR O CÓDIGO
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
