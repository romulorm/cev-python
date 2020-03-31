palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
             'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')

print('-=-' * 10)
print('VOGAIS NAS PALAVRAS'.center(30))
print('-=-' * 10)
for verbo in palavras:
    print('\nNa palavra {} temos '.format(verbo),end='')
    for letra in verbo:
        if letra in 'AEIOU':
            print('{}'.format(letra), end=' ')
