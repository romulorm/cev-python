'''Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada formatar() que consiga
 mostrar os números como um valor monetário formatado.'''

from utilidades.moeda import aumentar, diminuir, dobro, metade, formatar

preco = float(input('Digite o preço: R$ '))

print('O valor de {} com acréscimo de 15% é: {}'.format(formatar(preco), formatar(aumentar(preco, 15))))
print('O valor de {} com decréscimo de 10% é: {}'.format(formatar(preco), formatar(diminuir(preco, 15))))
print('O dobro de {} é: {}'.format(formatar(preco), formatar(dobro(preco))))
print('A metade de {} é: {}'.format(formatar(preco), formatar(metade(preco))))
