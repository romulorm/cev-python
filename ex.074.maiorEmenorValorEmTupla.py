from random import randint
numeros = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(n, end=' ')
print('\nO maior número foi o \33[32m{}\33[m.'.format(max(numeros)))
print('O menor número foi o \33[31m{}\33[m.'.format(min(numeros)))
