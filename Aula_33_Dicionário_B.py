'''
DICIONÁRIO E LOOPE FOR
'''
clientes = {
    'cliente1':
        {
    'blusa': 'cavalera',
    'calça': 'hering'
},
'cliente2':
    {
    'blusa':'tommy',
    'calça':'tommy'
},
    'cliente3':
        {'blusa':'dc',
        'calça':'tommy'}
}
# LOOPE FOR
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo{clientes_k}')
    for dados_k, dados_v in clientes.items():
        print(f'\t{dados_k}={dados_v}')


## TRANSFORMAR LISTA EM DICIONÁRIO
dicionario = [
    [1,'Paulo'],
    [2,'Carlos'],
    [3,'Eduardo'],
    [5, 'Barbara'],
    [6, 'Felipe'],
    [7, 'Pedro']
]
d5 = {2:'Novo', 3: 'mdb'}
print(dicionario)
## Casting
dicio = dict(dicionario)
print(dicio)
dicio.pop(1) # Eliminar uma chave, preciso dizer qual chave
print(dicio)
dicio.popitem() ## Eliminar o último item, idependente de qual seja esse item
print(dicio)
dicio.update(d5) ## Concatenar os dois dicionários
print(dicio)

















