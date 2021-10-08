'''
DICT COMPREHENSION
'''

lista = \
    [
    ('chave', '46'),
    ('chave_1', '63')
    ]

d1 = {x:y for x,y in lista} # o mesmo que dict(lista)

d2 = {x:(y*2) for x,y in lista} # o mesmo que dict(lista)

d3 = {x.upper():(y*2) for x,y in lista} # o mesmo que dict(lista)

d4 = {x:y for x,y in enumerate(range(5))}
print(d1)
print('')
print(d2)
print('')
print(d3)
print('')
print(d4)















