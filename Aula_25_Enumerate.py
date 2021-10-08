'''
ENUMERATE - Dúvidas
DESEMPACOTAR COM ENUMERATE - Gerando tuplas
'''

lista = [

    ['Paulo', 'Geraldo', 'Luis'],
    ['Guilherme', 'Bolsonaro', 'Filho04'],
    ['Lula', 'Paulinho', 'Jesus']
]

for v1, v2 in enumerate(lista):
    print(v1, v2)

print("**********************")

for v1, v2 in enumerate(lista, 53):
    print(v1, v2)

print("**********************")
# DESEMPACOTAR

for v1 in enumerate(lista):
    print(v1)