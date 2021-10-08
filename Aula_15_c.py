'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos,
escreva "Seu nome é curto", Se tiver entre 5 e 6 letras, escreva "Seu nome é normal", Maior que 6,
escreva, "Seu nome é muito grande."
'''
def nome():
    print(" ")
    print("############################################")
    print("######### PROGRAMA TAMANHO DO NOME #########")
    print("############################################")
    print("")
    nome = str(input("Nome: "))
    print("")
    tamanho = len(nome)
    if tamanho <= 4:
        print("Seu nome é pequeno.")
    elif 5 <= tamanho <= 6:
        print("Seu nome é normal.")
    elif tamanho > 6:
        print("Seu nome é grande.")
nome()