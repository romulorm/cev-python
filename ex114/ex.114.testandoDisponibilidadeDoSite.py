'''Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

from ex114.util import *

# PROGRAMA PRINCIPAL

site = 'http://www.pudim.com.br'
arquivo = 'logs.txt'

if verificaArquivo(arquivo):
    while True:
        registraLog(site, arquivo)
        sleep(5)






