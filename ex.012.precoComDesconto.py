preco = float(input('Digite o preço do produto: R$ '))
desconto = float(input('Digite o desconto (%): '))
valorDesconto = preco * (desconto / 100)
precoFinal = preco - preco * (desconto / 100)
print('-' * 28)
print('Valor do produto: R$ {:.2f}'.format(preco))
print('Desconto de {}%: R$ {:.2f}'.format(desconto, valorDesconto))
print('Valor final do produto: R$ {:.2f}'.format(precoFinal))
