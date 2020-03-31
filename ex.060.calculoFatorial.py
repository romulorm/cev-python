# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input("Informe um número: "))
r = 1
print('Calculando {}! = {}'.format(num, num),end='')
while num > 1:
    r = r * num
    num -= 1
    print(' x {}'.format(num), end='')
print(' = {}'.format(r))
