'''Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''

from ex114.util import *

# PROGRAMA PRINCIPAL

site = 'http://www.pudim.com.br'
arquivo = 'logs.txt'

if verificaArquivo(arquivo):
    print('Monitorando o site {}'.format(site))
    while True:
        registraLog(site, arquivo)
        sleep(5)
else:
    print('\33[31mO arquivo de log não está pronto!\33[m')





