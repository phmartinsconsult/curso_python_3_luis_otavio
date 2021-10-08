
print('List Comprehension')
lista = [1,2,3,4,5,6,7,8,9]
ex1 = [v+2 for v in lista if v%2==0]
print(ex1)
print()
print('If ternário')
x=90
ex2 = ['Par!' if x%6==0 else 'Impar!']
print(ex2)