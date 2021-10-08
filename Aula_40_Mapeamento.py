'''
FUNÇÃO MAPEAMENTO
'''


from dados import produtos, pessoas, lista, nova
# Importar uma função do notebook "dados"
nova(2,4)

# MAP é super idêntico a List Comprehension
nova_lista = map(lambda x: x*2, lista)
print(lista)
print(list(nova_lista))




















