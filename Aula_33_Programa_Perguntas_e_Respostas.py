'''
PROGRAMA DE PERGUNTAS E RESPOSTAS
'''
print()
print('************************************************************')
print("Leia as seguintes perguntas e indique as respostas corretas")
print('************************************************************')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2?',
    'respostas':
        {'a':'5',
         'b':'4',
         'c': '12',
         'd':'6'},
'resposta_certa':'b'
},
    'Pergunta 2': {
        'pergunta': 'Quanto é 20/4?',
        'respostas':
            {'a': '5',
             'b': '4',
             'c': '11',
             'd': '9'},
        'resposta_certa': 'a'
    },
'Pergunta 3': {
        'pergunta': 'Quanto é 38-4?',
        'respostas':
            {'a': '31',
             'b': '32',
             'c': '33',
             'd': '34'},
        'resposta_certa': 'd'
    }
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print("Respostas: ")
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]:{rv}')

    resposta_usuario = input("Resposta: ")

    if resposta_usuario == pv['resposta_certa']:
        print("Parabéns! Você acertou!")
        respostas_certas += 1
    else:
        print("Que pena! Você errou!")

    print()
    print('************************************************************')

    qtd_perguntas = len(perguntas)
    porcentagem_acerto = respostas_certas/qtd_perguntas*100

    print(f'Respostas corretas: {respostas_certas}.')
    print(f'Seu percentual de acerto é de {porcentagem_acerto:.2f}%.')
    print('************************************************************')





















