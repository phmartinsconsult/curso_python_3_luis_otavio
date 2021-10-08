'''
FOR e ELSE podem ser utilizados.
'''



variavel = ['Paulo', 'Alberto', 'Jorge', 'Carlos']

comeca_com_j = False

for valor in variavel:
    if valor.lower().startswith('j'):
        print(f'{valor} começa com J')
        comeca_com_j=True
        print(f'A palavra {valor} começa com J')
        continue
#else:
    #print("Essa palavra NÃO começa com J")
