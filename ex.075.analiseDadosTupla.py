'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num = (int(input('Digite um número: ')), int(input('Digite outro número: ')),\
      int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print('Você digitou os valores {}'.format(num))
print('O número \33[31m9\33[m apareceu \33[31m{}\33[m vezes.'.format(num.count(9)))
if num.count(3) == True:
    print('O valor \33[31m3\33[m apareceu na \33[31m{}ª\33[m Posição.'.format(num.index(3)+1))
else:
    print('O número 3 não foi digitado.')
print('Números \33[31mpares\33[m digitados: ',end='')
for n in num:
    if n % 2 == 0:
        print('\33[31m{}'.format(n), end=' ')
