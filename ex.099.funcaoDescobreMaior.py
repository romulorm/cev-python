'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
 inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep


def analisador(* num):
    maior = -999
    print('Analisando os valores passados...')
    for v in num:
        print(v, end=' ')
        sleep(0.3)
    print('=> Foram passados \33[35m{}\33[m valores.'.format(len(num)))
    for v in num:
        if v > maior:
            maior = v
    print('O maior número foi: \33[32m{}\33[m'.format(maior))


analisador(1, 4, 5, 7)
analisador(4, 8, 5)
analisador(5, 6, 5, 5, 5, 5, 5, 5, 5)

