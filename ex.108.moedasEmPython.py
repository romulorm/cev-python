'''Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada formatar() que consiga mostrar os números como um valor monetário formatado.'''

import moeda

preco = float(input('Digite o preço: R$ '))

print('O valor de {} com acréscimo de 15% é: {}'.format(moeda.formatar(preco), moeda.formatar(moeda.aumentar(preco, 15))))
print('O valor de {} com decréscimo de 10% é: {}'.format(moeda.formatar(preco), moeda.formatar(moeda.diminuir(preco, 15))))
print('O dobro de {} é: {}'.format(moeda.formatar(preco), moeda.formatar(moeda.dobro(preco))))
print('A metade de {} é: {}'.format(moeda.formatar(preco), moeda.formatar(moeda.metade(preco))))
