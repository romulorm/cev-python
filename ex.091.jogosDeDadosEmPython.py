'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses
 resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
  número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
}
for k, v in jogo.items():
    print('O {} tirou {} no dado.'.format(k, v))
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=-' * 10)
print('-----------RANKING-----------')
print('-=-' * 10)
for i, v in enumerate(ranking):
    print('{}º lugar: {} com {} ponto(s).'.format(i+1, v[0], v[1]))
    sleep(1)