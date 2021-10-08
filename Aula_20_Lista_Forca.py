

def forca():
    print('***************************************')
    print('********** JOGO DA FORCA **************')
    print('***************************************')
    print(" ")
    print(" ")
    secreto = 'perfume'
    digitadas = []
    chances = 3

    while True:
        if chances <= 0:
            print('Você perdeu!!!')
            break ## Parar o meu código quando ele não tiver mais chances

        letra = input('Digite uma letra: ')

        if len(letra) > 1:
            print('Ahhh isso não vale, digite apenas uma letra.')
            continue ## Mudar para a próxima etapa.

        digitadas.append(letra)

        if letra in secreto:
            print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
        else:
            print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
            digitadas.pop()

        secreto_temporario = ''
        for letra_secreta in secreto:
            if letra_secreta in digitadas:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += '*'

        if secreto_temporario == secreto:
            print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
            break
        else:
            print(f'A palavra secreta está assim: {secreto_temporario}')

        if letra not in secreto:
            chances -= 1

        print(f'Você ainda tem {chances} chances.')
        print()
forca()


