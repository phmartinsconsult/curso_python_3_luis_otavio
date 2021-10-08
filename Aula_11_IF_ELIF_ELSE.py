
def emprestimo():
    print('***************************************')
    print('*** ALGORÍTMO DO CRÉDITO CONSIGNADO ***')
    print('***************************************')
    print(" ")
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    renda = float(input("Digite sua renda: "))
    idade_menor = 20
    idade_maior = 30
    renda_maior = 5000
    print(" ")
    if idade >= idade_menor and idade <= idade_maior and renda >= renda_maior:
        print(f'{nome}, você pode pegar o empréstimo.')
    else:
        print(f'{nome}, infelizmente, você NÃO pode pegar o empréstimo.')
emprestimo()