
'''
DESEMPACOTAMENTO DE LISTAS
'''

lista = ['Luiz', 'João', 'Maria', 1,2,3,4,5]
# Cada valor da lista será uma variável abaixo
#n1, n2, n3 = lista
n1, n2, *outralista = lista ## Mostra apenas os valores de n1

print(lista)
print(n2) # Podemos colocar outros valores também

