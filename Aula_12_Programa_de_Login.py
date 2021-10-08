

print('******************************************************')
print('******** LOGIN NO SISTEMA INTERNO DA LOJA ************')
print('******************************************************')
print("")
usuario = str(input("Usuário: " ))
senha = int(input("Senha: "))
cpf = str(input("CPF: "))
print("******************************************************")
print("")
usuario_bd = "Paulo"
senha_bd = 123456
cpf_bd = '07937402660'
if usuario == usuario_bd and senha == senha_bd and cpf == cpf_bd:
    print(f'Usuário digitado: {usuario}')
    print(f'Senha digitada: {senha}')
    print(f'CPF digitado: {cpf}')
    print("Você está conectado no sistema interno da loja.")
else:
    print(f'Usuário digitado: {usuario}')
    print(f'Senha digitada: {senha}')
    print(f'CPF digitado: {cpf}')
    print("Login, Senha ou CPF incorretos. Tente novamente.")




