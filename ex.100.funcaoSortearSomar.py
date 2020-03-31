'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
 a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep

numeros = list()

def sortear(lista):
    """
    Sorteia 5 números e inclui em uma lista.
    :param lista: É a lista recebida
    :return: sem retorno
    """
    print('Sorteando 5 valores: ')
    for c in range(0, 5):
        n = (randint(1, 10))
        lista.append(n)
        print(n, end=' ')
        sleep(0.5)
    print('PRONTO!')


def somarPar(lista):
    """
    Soma somente os números pares da lista.
    :param lista: lista de números.
    :return: sem retorno
    """
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print('A soma dos valores pares é: \33[31m{}\33[m'.format(soma))

# Programa Principal

sortear(numeros)
somarPar(numeros)
help(somarPar)