from random import randint

soma = 0
cont = 0
tipo = ' '
print('=-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR!')
print('=-=' * 20)
while True:
    valorPlayer = int(input('\033[mDigite um valor: '))
    valorCPU = randint(0, 10)
    soma = valorPlayer + valorCPU
    opcaoPlayer = str(input('Par ou Ímpar? [P/I]').upper().strip()[0])
    if soma % 2 == 0:
        tipo = 'P'
    else:
        tipo = 'I'
    print('Você jogou {} e o computador {}. Total de {} deu {}.'.format(valorPlayer, valorCPU, soma, tipo))
    if opcaoPlayer == tipo:
        print('\033[32mVocê VENCEU!! Vamos jogar novamente...')
        cont += 1
    else:
        print('\033[31mVocê PERDEU! Game Over!')
        break
print('\033[33mVocê obteve {} vitórias consecutivas.'.format(cont))
print('\033[34mAperte o PLAY novamente para jogar.')
