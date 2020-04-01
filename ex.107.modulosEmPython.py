'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''

import moeda

preco = float(input('Digite o preço: R$ '))

print('O valor de R$ {} com acréscimo de 15% é: R$ {}'.format(preco, moeda.aumentar(preco, 15)))
print('O valor de R$ {} com decréscimo de 10% é: R$ {}'.format(preco, moeda.diminuir(preco, 10)))
print('O dobro de R$ {} é: R$ {}'.format(preco, moeda.dobro(preco)))
print('A metade de R$ {} é: R$ {}'.format(preco, moeda.metade(preco)))
