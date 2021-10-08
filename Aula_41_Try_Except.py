'''
TRY AND EXCEPT - TRATANDO EXCESSÕES
Muito similar a IF e ELSE
Porém, neste caso, estamos tratando as excessões.
'''

try:
    a = {}
    print(a[1])
except NameError as erro:
    print('Erro do desenvolvedor, fale com o Desenvolvedor.')
except (IndexError, KeyError) as erro:
    print('Erro de índice')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    print('Seu código foi executado com sucesso.')
    print(a)
finally:
    print('Finalmente')

print('Bora continuar...')





