'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
 lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem
  crescente.'''

numeros = [[], []]

for n in range(1, 8):
    valor = int(input('Digite o {}º valor: '.format(n)))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('Lista de números digitados: {}'.format(numeros))
print('Números pares em ordem: {}'.format(sorted(numeros[0])))
print('Números ímpares em ordem: {}'.format(sorted(numeros[1])))