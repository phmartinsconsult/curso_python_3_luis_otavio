'''
DICIONÁRIOS - CHAVE E VALOR
Dicionário = {'Chave':'Valor'}
'''

d1 = {'Paulo': 32}
d1['Guilherme'] = 31 # Incluindo novas informações ao dicionário.
d1['Izabela'] = 38
d1['Aline'] = 36
d1['Paula'] = 37
print(d1)
print(d1['Paulo']) # Acessar uma chave específica
d1.update({'novachave':'novo_valor'})
del d1['Paula'] # Deletar uma das chaves

d2 = {
    123 : 'Paulo',
    (7,6,5): 'Tupla',
    156: 'Outro valor'
}
print(d2)
print(d2[(7,6,5)])
d2[123] = 'Viviane' # Mudar um valor dentro do dicionário

# Verificando
if 123 in d2:
    print('Valor presente')
else:
    print('Valor não está presente')

print(d2.get(123)) ## Localizar um valor dentro do meu dicionário.
if (d2.get(123)) is not None:
    print(d2.get(123))
else:
    print("Chave não existe")

print(123 in d2) # Verificar se a chave é True.
print(123 in d2.keys()) # Verificar se a chave é True.
print('Paulo' in d2.values()) # Verificar se um dos valores é True.
print(len(d2)) # Quantos pares de chave


for k in d2:
    print(k)

for k in d2.values():
    print(k)

for k in d2.items():
    print(k)

for k in d2.items():
    print(k[0], k[1])

d3 = {
    1: 'Paulo',
    2: 'Alberto',
    3: 'Carlos'
}
v = d3 # Mesmos objetos na memória - POO.
v1 = d3.copy() # Objetos diferentes na memória.
v1[2] = 'Melissa'
print(d3)
print(v)
print(v1)


























