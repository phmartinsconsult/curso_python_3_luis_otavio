'''
Use f strings para não precisar de usar as virgulas.
{imc:.f} = representa o número de casas decimais que queremos apresentar na frase.
'''


def apresenta():
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    e_maior = idade > 18
    peso = int(input("Digite seu peso: "))
    imc = peso/(altura**2)
    print(" ")
    print(f'{nome} tem {idade} anos e seu imc é {imc:.2f}.')
    print("{} tem {} anos e seu imc é {:.2f}.".format(nome,idade,imc))
    if imc <= 25:
        print("Parabéns, seu peso está excelente! =)")
    else:
        print("Cuidado! Você pode ter uma vida mais fit.")
apresenta()
