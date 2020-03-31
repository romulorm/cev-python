'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
opcao = 'S'
pessoas = list()
temp = list()
maior = 0
menor = 300

while opcao == 'S':
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if temp[1] > maior:
        maior = temp[1]
    if temp[1] < menor:
        menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    opcao = str(input('Deseja continuar? [S/N]').strip().upper()[0])
print('Ao todo você cadastrou {} pessoas.'.format(len(pessoas)))
print('O maior peso de {} foram das pessoas: .'.format(maior), end=' ')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print('\n')
print('O menor peso de {} foram das pessoas: .'.format(menor), end=' ')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
