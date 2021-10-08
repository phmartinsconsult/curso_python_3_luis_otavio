
""""
## Vamos falar sobre a função print
print("Paulo", "e", "Vivi")
print("Paulo", "e", "Vivi", sep="-", end="....")
print("Paulo", "e", "Vivi", sep="-")
print("Paulo", "e", "Vivi", sep="-")
print(" ")
print("079", "374", "026", sep=".", end="-")
print("60")
print()
print()
"""

def fun_cpf():
    a = str(input("Insira o primeiro trio de números do CPF: "))
    b = str(input("Insira o segundo trio de números do CPF: "))
    c = str(input("Insira o terceiro trio de números do CPF: "))
    d = str(input("Insira os dois últimos números do CPF: "))

    print(" ")

    print("O CPF digitado é:", end=" ")
    print(a,b,c, sep=".", end="-")
    print(d)
fun_cpf()


















