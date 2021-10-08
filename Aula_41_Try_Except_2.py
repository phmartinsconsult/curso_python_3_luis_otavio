
def divide(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError as error:
        print('Log:', error)
        raise

# Erro: tentar dividir por zero.
try:
    print(divide(2,0))
except ZeroDivisionError as error:
    print(error)


# Desenvolvedor não coloca mensagens sem sentido para usuário final.
# Para usuário final sempre usamos mensagens completas.



