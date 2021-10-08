
carrinho_do_site = []
carrinho_do_site.append(('Produto 1',30))
carrinho_do_site.append(('Produto 2',35))
carrinho_do_site.append(('Produto 3',20))
carrinho_do_site.append(('Produto 4',22))

print(carrinho_do_site[0][1])
print(carrinho_do_site[1][1])
print(carrinho_do_site[2][1])
print(carrinho_do_site[3][1])
print(carrinho_do_site)

#Desempacotamento
produto, preço = carrinho_do_site[0]
print(produto, preço)
print(f'O preço do {produto} é R${preço},00')

#total = ((x,y) for x,y in carrinho_do_site)
#print(total)
total = sum(y for x,y in carrinho_do_site)
print(total)



