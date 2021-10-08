print('********************************************************')
print('***************** ALGORITMO DA BOVESPA *****************')
print('********************************************************')
print("")

def bolsa(percent, valor_atual):
    valor_atual = int(valor_atual)
    ganho_anual = float(input("Ganho médio anual: "))

    if percent >= 2:
        valor_invest = 0.5 * valor_atual
    elif percent >= 0 and percent <2:
        valor_invest = 0.2 * valor_atual
    elif percent <0 and percent >= -2:
        valor_invest = 0.6 * valor_atual
    elif percent <= -2:
        valor_invest = 0.9 * valor_atual
    else:
        valor_invest = 0

    patrimonio_total = valor_invest + valor_atual
    patrimonio_1_ano_depois = patrimonio_total * ganho_anual
    return valor_invest, patrimonio_total, patrimonio_1_ano_depois
########################################################################
valor_atual = int(input("Valor atual da carteira: "))
percent = float(input("Percentual de variação nas ações: "))
bolsa_exec = bolsa(percent, valor_atual)

print(f'O valor total investido na bolsa é de R${bolsa_exec[0]:.2f}.')
print(f'O patrimônio total investido será de R${bolsa_exec[1]:.2f}.')
print(f'Após um ano o investimento rendeu R${bolsa_exec[2]:.2f}.')


