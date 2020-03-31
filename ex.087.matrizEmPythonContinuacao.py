'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

num = maior = coluna3 = somaPar = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input('Digite um valor para [{},{}]: '.format(linha, coluna)))
        matriz[linha][coluna] = num
        if num % 2 == 0:
            somaPar += num
        if coluna == 2:
            coluna3 += num
        if linha == 1 and num > maior:
            maior = num

for linha in range(0, 3):
    for coluna in range(0, 3):
        print('[{:^5}]'.format(matriz[linha][coluna]), end='')
    print()
print('A soma de todos os valores pares é: {}'.format(somaPar))
print('A soma dos valores da terceira coluna é: {}'.format(coluna3))
print('O maior valor da segunda linha é: {}'.format(maior))
