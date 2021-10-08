'''
* Criar variáveis com nome (str), idade (int), altura (float) e peso (float) de uma pessoa.
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (baseado no peso e altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-String (com as chaves)
'''

def descricao():
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite o seu peso: "))
    print("")
    ano_atual = 2021
    ano_nascimento = ano_atual - idade
    imc = peso/(altura**2)
    print(f'{nome} tem {idade} anos e {altura} de altura.')
    print(f'{nome} pesa {peso} kg e nasceu em {ano_nascimento}.')
    print(f'{nome} tem o IMC de: {imc:.2f}.')
    if imc <= 25:
        print(f'Parabéns {nome}, seu imc está muito bom!')
    else:
        print(f'Cuidado {nome}! Seu imc está elevado!')
descricao()