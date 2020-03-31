'''
Posição par = Produto
Posição ímpar = Preços
'''

produtos = ('Borracha', 1.75,
            'Caneta', 1.00,
            'Lapiseira', 8.99,
            'Mochila', 129.00,
            'Caderno', 15.99,
            'Livro', 32.00,
            'Estojo', 15.99,
            'Compasso', 5.99)
print('-=-' * 13)
print('LISTAGEM DE PRODUTOS'.center(40))
print('-=-' * 13)

for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print('{:.<30}'.format(produtos[posicao]),end=' ')
    else:
        print('R$ \33[31m{:>7.2f}\33[m'.format(produtos[posicao]))