'''
Inicia com letra, pode conter números, separar_, letra minúscula.
Variável = apelido que damos para algo que vamos manter na memória.
'''


def apresenta():
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    e_maior = idade > 18
    peso = int(input("Digite seu peso: "))
    imc = peso//(altura**2)
    print(" ")
    print(nome, "tem", idade, "anos e seu imc é", imc,".")
    if imc <= 25:
        print("Parabéns, seu peso está excelente! =)")
    else:
        print("Cuidado! Você pode ter uma vida mais fit.")
apresenta()