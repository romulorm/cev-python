'''Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
 informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

from utilidades.moeda import aumentar, diminuir, dobro, metade, formatar

preco = float(input('Digite o preço: R$ '))

print('O valor de {} com acréscimo de 15% é: {}'.format(formatar(preco), aumentar(preco, 15, True)))
print('O valor de {} com decréscimo de 10% é: {}'.format(formatar(preco), diminuir(preco, 15, True)))
print('O dobro de {} é: {}'.format(formatar(preco), dobro(preco, True)))
print('A metade de {} é: {}'.format(formatar(preco), metade(preco, True)))
