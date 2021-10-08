
print("********************************************")
print("****** CONTADOR DE PALAVRAS EM FRASES ******")
print("********************************************")
print()
print()
## SPLIT

string = "O Brasil é um país top, eu o amo!"
lista1 = string.split(' ') # Separa utilizando o espaço
lista2 = string.split(',') # Separar utilizando as virgulas

for valor in lista1:
    print(f'A palavra "{valor}" apareceu {lista1.count(valor)}x na frase.')
print('#############################################')
for valor in lista2:
    print(valor.strip()) # 