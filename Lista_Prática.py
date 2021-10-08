
print('******** AULA PRÁTICA ********')

def pratica():
    lista = []
    for a in range(1,10):
        valor = int(input(f'Diga o valor número {a} da sua lista: '))
        lista.append(valor)
    print()
    #lista = [1,2,3,4,5,6,7,8,9]
    print(f'O primeiro valor da lista é: {lista[0]}')
    print(f'O segundo valor da lista é: {lista[1]}')
    print(f'O terceito valor da lista é: {lista[2]}')
    print(f'A soma dos 3 primeiros valores da lista é: {(sum(lista[0:3])):.2f}')
    print(f'O último valor da lista é: {lista[-1]}')
    print(f'O penultimo valor da lista é: {lista[-2]}')
    print(f'O antipenultimo valor da lista é: {lista[-3]}')
    print(f'A média dos 3 últimos valores da lista é: {((sum(lista[-3:-1]))/3):.2f}')
    print()
    for i in lista:
        i2 = i + 2
        print(f'O valor de {i} + 2 é igual a {i2}')
    print()
    for i in lista:
        if i % 2==0:
            print(f'O valor {i} é par.')
    print()
    for i3 in range(2,10):
        i4 = i+i3
        print(f'{i} + {i3} = {i4}')
pratica()



































