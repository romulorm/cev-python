'''Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''
from time import sleep
from urllib import request
from datetime import datetime

while True:
    sleep(5)
    try:
        site = request.urlopen('http://www.pudim.com.br')
    except:
        print('Não acessível\t{}'.format(datetime.now()))
    else:
        print('OK\t{}'.format(datetime.now()))

