# Exercício Python 011: Calcular a qtde necessária de tinta para pintar um cômodo, sabendo que 1L de tinta pinta 2m
# quadrados.

largura = float(input('Escreva a largura do cômodo: '))
altura = float(input('Escreva a altura do cômodo: '))
metragem = largura * altura
tinta = metragem / 2
print('Você precisará de {} litros de tinta para pintar um cômodo de {} metros quadrados'.format(tinta, metragem))