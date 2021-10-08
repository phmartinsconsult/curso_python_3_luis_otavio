



def fun(*args, **kwargs):
    print(f'Todos os args: {args}')
    print(f'O primeiro argumento da lista é: {args[1]}')
    print(f'Todos os Key words arguments são: {kwargs}')
    print(kwargs['nome'] + " " + kwargs['sobrenome'])
    print(kwargs['sobrenome'])
    print()
    nome = kwargs.get('nome') # Melhor usar o Get
    idade = kwargs.get('idade')
    print()
    if idade == None:
        print("Idade inexistente")
    else:
        print(idade)


lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
fun(*lista1, *lista2, nome='Luis', sobrenome= 'Martins')
# Kwargs retorna um dicionário