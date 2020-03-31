'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o
nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''


jogador = dict()
listaGols = list()
numpartidas = 0
jogador['nome'] = str(input('Nome: '))
for j in range(1, 6):
    numGol = int(input('Quantos gols na partida {}? '.format(j)))
    numpartidas += 1
    listaGols.append(numGol)
jogador['gols'] = listaGols
jogador['total'] = sum(listaGols)
print('-=-' * 20)
print(jogador)
print('-=-' * 20)
for k, v in jogador.items():
    print('O campo {} tem o valor {}.'.format(k, v))
print('-=-' * 20)
print('O jogador {} jogou {} partidas.'.format(jogador['nome'], numpartidas))
for k, v in enumerate(jogador['gols']):
    print('    => Na partida {}, fez {} gols.'.format(k + 1, v))
print('Foi um total de {} gols.'.format(jogador['total']))
