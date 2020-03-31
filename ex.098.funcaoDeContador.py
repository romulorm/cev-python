'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
 fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep


def contagem(inicio, fim, passo):
     prox = 0
     if inicio < fim:
        print('\33[32mContagem de {} até {} de {} em {}\33[m'.format(inicio, fim, passo, passo))
        for n in range(inicio, fim + 1, passo):
            print(n, end=' ')
            sleep(0.5)
        print('FIM!')
        print('-=-' * 12)
     elif inicio > fim:
        print('\33[32mContagem de {} até {} de {} em {}\33[m'.format(inicio, fim, passo, passo))
        for n in range(inicio, fim + passo, passo):
            print(n, end=' ')
            sleep(0.5)
        print('FIM!')
        print('-=-' * 12)
     elif inicio < 0:
        print('\33[32mContagem de {} até {} de {} em {}\33[m'.format(inicio, fim, passo, passo))
        print(inicio, end=' ')
        while inicio <= fim:
            prox = inicio + passo
            print(prox, end=' ')
            sleep(0.5)
        print('FIM!')
        print('-=-' * 12)

# Programa Principal
contagem(1, 10, 1)
contagem(10, 0, -2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)
