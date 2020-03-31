frase = str(input('Digite uma frase: ').strip().upper())
qtde = frase.count('A')
posFirst = frase.find('A')
posLast = frase.rfind('A')
print('A letra A aparece {} vezes na frase.'.format(qtde))
print('A primeira letra A apareceu na posição {}'.format(posFirst + 1))
print('A última letra A apareceu na posição {}'.format(posLast + 1))

