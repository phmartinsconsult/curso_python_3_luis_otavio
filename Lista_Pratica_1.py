
print()
l1 = [
    'Paulo',
    'Alberto',
    'Daniel',
    'Guilherme',
    'Sebastião'
]
l1.sort()
l1.append('Paulenice')
l1.append('Isaque')
print(f'O primeiro parâmetro da lista é: {l1[0]}.')
print(f'O último elemento da lista é: {l1[-1]}.')
print(f'Esta lista possui {len(l1)} elementos.')
for i in l1:
    print(f'Um dos nomes da lista é: {i}.')

if 'Paulo' in l1:
    print('Paulo')

print()
l2 = [
    10,
    15,
    18,
    20,
    9,
    5,
    4,
    3
]

contador = 0
for i in l2:
    contador += i
    print(contador)




