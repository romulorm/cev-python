maior = []
menor = []
lista = []
for v in range(0, 5):
    lista.append(int(input('Digite um valor para a Posição {}: '.format(v))))
print('Você digitou os valores {}.'.format(lista))
maximo = (max(lista))
minimo = (min(lista))
for pos, valores in enumerate(lista):
    if valores == max(lista):
        maior.append(pos)
    if valores == min(lista):
        menor.append(pos)
print('O maior valor foi {} e apareceu nas posições:'.format(maximo, maior), end=' ')
for n in maior:
    print(n, end=' ')
print('\nO menor valor foi {} e apareceu nas posições:'.format(minimo, menor), end=' ')
for n in menor:
    print(n, end=' ')
