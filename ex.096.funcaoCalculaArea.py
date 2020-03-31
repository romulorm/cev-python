'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a área do terreno.'''

def calculaArea(larg, comp):
    a = larg * comp
    print('A área de um terreno \33[33m{}\33[m x \33[33m{}\33[m é de \33[32m{}m2\33[m.'.format(larg, comp, a))


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
calculaArea(l, c)
