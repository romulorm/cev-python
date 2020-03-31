n = total = maior = media = cont = 0
menor = 9999999999
opcao = 'S'
while opcao == 'S':
    n = int(input('Digite um número: '))
    total += n
    cont += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    opcao = str(input('Quer continuar? [S/N]: ').strip().upper()[0])
media = total / cont
print('\033[32mVocê digitou {} números e a média foi {:.1f}.'.format(cont, media))
print('\033[31mO maior valor foi {} e o menor valor foi {}.'.format(maior, menor))