'''
VARIÁVEL LOCAL E GLOBAL
'''

variavel = 'valor'

def func():
    print(variavel)

def func2():
    variavel = 'Outro valor'
    print(variavel)

func()
func2()