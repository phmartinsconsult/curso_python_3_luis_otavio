

print("******************************************")
print("***** PROGRAMA TROCADOR DE VARIÁVEIS *****")
print("******************************************")
print()
x = int(input("Valor de x: "))
y = str(input("Valor de y: "))
z = float(input("Valor de z: "))
x,y,z = z,y,x ## Trocando os valores das variáveis
print()
print(f'Os valores das variáveis são: x={x}, y={y} e z={z}')

