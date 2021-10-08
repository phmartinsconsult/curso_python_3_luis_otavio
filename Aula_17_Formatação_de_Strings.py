

print("****************************************")
print("****** FORMATAÇÃO DE STRINGS ***********")
print("****************************************")
print("")
# Manipultando as strings
# String indices

# I. Positivos     [01234]
nome             = 'Paulo'
# I. Negativos     [54321]
site = 'www.home.com.br/'
print(f'O índice solicitado recebe a letra: {nome[2]} ou {nome[2].upper()} ')
#print(f'O índice solicitado recebe a letra: {nome[9]} ou {nome[9].upper()} ') ## Erro pq não tem o 9
print(f'{site[:-1]}, não possui barra.')
print(nome[1:4]) # Printar apenas uma parte do nome






