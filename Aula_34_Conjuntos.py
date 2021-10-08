'''
SET - CONJUNTOS
'''

s1 = {1,2,3,4,5} # Conjunto
for v in s1:
    print(v)

s2 = set()
s2.add(1) # Adicionar valor ao conjunto.
s2.add(2)
s2.add(3)
s2.add(4)
s2.add((5,6, 7, 'Paulo'))
print(f'O meu conjunto possui os seguintes elementos: {s2}')
s2.discard(1) ## Retirar um elemento do meu dicionário.

s2.update([1,2,3,4,5],{5,6,7}) #Note que não duplica elementos
print(s2)

s3 = [1,2,3,4,5,3,4,4,5,,2,2,3,4] # Era uma lista
s3 = set(s3) # Transformei em um dicionário.
s3 = list(s3) # Transformei novamente em uma lista




















