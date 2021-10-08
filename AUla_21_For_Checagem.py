


variavel = ['Paulo','Carlos', 'Alberto'] # Variavel lista

for valor in variavel:
    print("Começando o FOR")
    print("Verificar a primeira condição.")
    if valor.startswith('A'):  ## Começa com a letra 'A'
        print("Primeira condição correta")
        print(f'Resultado: a palavra começa com A, {valor}')
        print('Primeira condição verificada')
    else:
        print('Primeira condição NÃO satisfeita. Verificar a segunda condição')
        print(f'Resultado: a palavra NÃO começa com A, {valor}')
        print("Segunda condição verificada")

