maisDeMil = total = 0
prodMaisBarato = ' '
precoMaisBarato = 99999999999999
print('-=-' * 10)
print(' \033[33m--- LOJA SUPER BARATÃO ---\033[m ')
print('-=-' * 10)
while True:
    nomeProduto = str(input('Nome do Produto: '))
    precoProduto = float(input('Preço do Produto: '))
    if precoProduto < precoMaisBarato:
        precoMaisBarato = precoProduto
        prodMaisBarato = nomeProduto
    total += precoProduto
    if precoProduto > 1000:
        maisDeMil +=1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ').upper().strip()[0])
    if opcao == 'N':
        break
print('-=-' * 18)
print('\033[31mTotal em compras: R$ {:.2f}'.format(total))
print('\033[33mTemos {} produtos custando mais de R$ 1000,00.'.format(maisDeMil))
print('\033[32mO produto mais barato foi {} com o preço de {:.2f}.'.format(prodMaisBarato, precoMaisBarato))
