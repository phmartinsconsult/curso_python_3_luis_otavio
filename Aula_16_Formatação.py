

def divisao():
    print('************************************')
    print('***** PROGRAMA DE FORMATAÇÃO *******')
    print('************************************')
    print(" ")
    nome = input('Nome: ')
    numero1 = int(input("Primeiro número: "))
    numero2 = int(input("Segundo número: "))
    divisao = numero1/numero2
    print("")
    print('Algumas formatações interessantes:')
    print("")
    print(f'{nome:s}, o resultado da divisão é {divisao:.2f}.')
    print(f'Utilizando formatadores notamos que podemos ter um número 1 com 10 numeros: {numero1:0>10}.')
    print(f'Número formatado duas vezes: {divisao:0>10.2f}')
    print(f'Posso formatar meu nome também: {nome:@>6}')
    print('{} também posso colocar assim'.format(nome))
    print(nome.lower())
    print(nome.upper())
    print(nome.title())
divisao()

# Formatar como string
