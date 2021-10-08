'''
MEMORIZE
'''

n_acessos = [
    4,
    5,
    90,
    32,
    109,
    88
]

for numero in n_acessos:
    if numero % 2 == 0:
        print(f'O numero {numero} é par.')
    else:
        print(f'O numero {numero} é impar')

print()
for numero in range(10, 21):
    if numero % 2 == 0:
        print("O número", numero, "é par")

pessoas = [
    ({
        'nome': 'João',
        'cidade': 'Belo Horizonte'
    }),
    ({
        'nome': 'Maria',
        'cidade': 'São Paulo'
    }),
    ({
        'nome': 'Pedro',
        'cidade': 'Curitiba'
    })]

contador = 0
for pessoa in pessoas:
    contador += 1
    if pessoa['nome'] == 'Maria':
        continue
    print(contador)
    print(pessoa['nome'], "mora em", pessoa['cidade'])





