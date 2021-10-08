'''
GROUP BY - ITERTOOLS - Agrupar dados que estão em um dicionário
'''

from itertools import groupby

alunos = [
    {'nome': 'Luis', 'nota':'A'},
    {'nome': 'Paulo', 'nota':'B'},
    {'nome': 'Alberto', 'nota':'D'},
    {'nome': 'Carlos', 'nota':'A'},
    {'nome': 'Noberto', 'nota':'C'},
    {'nome': 'Pablo', 'nota':'D'},
    {'nome': 'Viviane', 'nota':'B'},
    {'nome': 'Eleotério', 'nota':'A'},
    {'nome': 'Gilvan', 'nota':'C'},
    {'nome': 'Laura', 'nota':'D'}
]

'''
# Ordenar os nomes
alunos.sort(key=lambda item:item['nota']) #Dados Ordenados
for alunos in alunos:
    print(alunos)
'''

# Agrupar os nomes
ordena = (lambda item: item['nota'])
alunos.sort(key=ordena) # Necessário sempre ordenar!!
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')

    quantidade = len(list(valores_agrupados))
    print(f'{quantidade} de alunos tiraram nota {agrupamento}')
    #for alunos in valores_agrupados:
        #print(alunos)




















