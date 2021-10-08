'''
Operadores ternários
'''

logged_user = True

if logged_user:
    print()
    msg = 'Usuário logado!'
else:
    print()
    msg =  'Usuário precisa logar!'

print(msg)

# Operadores ternários: simplificam as condições
# Podemos simplificar isso:

msge = 'Usuário logado!' if logged_user else 'Usuário precisa logar.'
print(msge)