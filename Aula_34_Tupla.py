'''
TUPLAS: Iigual às listas, porém não pode editar/alterar elementos.
'''

tupla1 = (1, 4, 9, "Paulo", "Sebastião")
print(f'A Tupla 1 é: {tupla1}.')
print(f'O quinto elemento da Tupla 1 é: {tupla1[4]}.')
print(f'O quarto elemento da Tupla 1 é: {tupla1[3]}.')
print(f'O último elemento da Tupla 1 : {tupla1[-1]}.')
print(f'Os dois últimos elementos da Tupla 1 são: {tupla1[-2:]}.')
print('Vamos criar um loop FOR com essa Tupla 1')
for v in tupla1:
    print(v)
print()
# Podemos criar uma tupla sem parenteses

tupla2 = 1,2,3,4,5,"Paulo" ## Criando a Tupla 2
tupla3 = 7,8,9,10
concatupla4 = tupla2 + tupla3 # Concatenar a tupla
print(f'A concatenação das listas gera: {concatupla4}.')
print(tupla2, tupla3, type(tupla2), type(tupla3))
# Podemos empacotar também

n0, n1, n2, n3, *args, n10 = concatupla4 # Estamos empacotando a concatupla4
print(n3)
print(n10)
print(n0)

# Podemos transformar uma tupla em uma lista
# Para alterar um valor de uma Tupla, basta transformá-la em uma lista
tupla5 = list(tupla2)
print(tupla5)
print(tupla5[4])
tupla5[4] = 30000
print(tupla5[4])
print(tupla5)


















