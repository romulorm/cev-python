print('-=-' * 12)
print('Sequência de Fibonacci')
print('-=-' * 12)
q = int(input('Quantos termos você quer mostrar? '))
c = 0
num = 1
ant = 0
aux = 0
r = 0
print('{} -> {}'.format(ant, num), end='')
while c < q -2:
    aux = ant
    ant = num
    num += aux
    c += 1
    print(' -> {}'.format(num), end='')
print(' -> FIM')