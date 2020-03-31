'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
 quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from time import sleep
from random import randint

cartela = [0, 0, 0, 0, 0, 0]
cont = numero = 0

print('-=-' * 12)
print('-------- \33[34mJOGO DA MEGA SENA\33[m --------')
print('-=-' * 12)
quantidade = int(input('Digite o número de jogos: '))
for j in range(0, quantidade):
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in cartela:
            cartela[cont] = numero
            cont += 1
        if cont == 6:
            break
    print('\33[32mJogo {}\33[m: \33[31m{}\33[m'.format(j + 1, sorted(cartela)))
    sleep(1)
print('---------- \33[34mBOA SORTE!\33[m -----------')
