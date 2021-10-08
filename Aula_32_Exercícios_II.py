


def mestre(funcao, *args, **kwargs): ## O que essa função faz? Ela REPASSAR os parâmetros.
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'Luis')
executando2 = mestre(saudacao, 'Luis', saudacao="Bom dia!")
print(executando)
print(executando2)

# Chamando a função mestre, que recebe a função fala_oi e outros parâmetros também.
#








