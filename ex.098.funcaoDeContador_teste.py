'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início,
 fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

from time import sleep

def contagem(inicio, fim, passo):
    prox = 0
    print('Contagem de {} até {} de {} em {}'.format(inicio, fim, passo, passo))
    print(inicio, end=' ')
    while inicio <= fim:
        prox = inicio + passo
        print(prox, end=' ')
    print('FIM!')
    print('-=-' * 12)


print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contagem(i, f, p)