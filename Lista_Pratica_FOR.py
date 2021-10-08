print('**********************************************')
print('**************** FUNÇÃO LOOPE ****************')
print('**********************************************')
print(0)

def for_i():
    print('Começou')
    lista_n = []
    print('Entrou no FOR')
    for i in range(1,9):
        i2 = i + 2
        if i2 % 2==0:
            lista_n.append(i2)
        print(f'O valor real é {i} e seu multiplo é {i2}.')
    print(f'A lista completa de números novos: {lista_n}.')
for_i()
print()
def novo():
    lista = []
    for i in range(1,9):
        nome = str(input("Nome: "))
        if nome.startswith("P") and nome.capitalize():
            lista.append(nome)
    print(f'A lista de nomes é a seguinte: {lista}')
novo()







