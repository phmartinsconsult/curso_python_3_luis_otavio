'''
LIST COMPREHENSION - EXERCÍCIOS
'''


string = '123456789123456789123456789123456789123456789123456789123456789'

# Solução

n = 10
lista = [string[i:i+n] for i in range (0, len(string), n)]
retorno = '.'.join(lista)
print(lista)
print(retorno)

























