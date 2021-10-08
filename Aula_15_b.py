'''
Faça um programa que peça ao usuário a hora, baseando-se na hora apresentada,
exiba a saudação apropriada. Por exemplo, Bom dia!, Boa tarde!, Boa noite!
'''
def relogio():
    print(" ")
    print("***********************************************")
    print("************* PROGRAMA DO RELÓGIO *************")
    print("***********************************************")
    print(" ")
    horas = int(input("Digite quantas horas exatas são agora: "))
    print(" ")
    if horas >= 6 and horas <= 12:
        print("Bom dia! Deus abençoe seu dia!")
    elif horas >= 13 and horas <= 18:
        print("Boa tarde! Deus abençoe sua tarde!")
    elif horas >= 19:
        print("Boa noite! Deus abençoe sua noite!")
relogio()