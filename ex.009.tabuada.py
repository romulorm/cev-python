numero = int(input('Escreva um número inteiro: '))
i = 1
print('-' * 15)
print('Tabuada de', numero)
print('-' * 15)
while i < 11:
  resultado = numero * i
  print('{} * {} = {}'.format(numero, i, resultado))
  i = i + 1
