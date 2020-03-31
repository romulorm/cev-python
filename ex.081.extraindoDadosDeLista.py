lista = []
opcao = 'S'
cont = 0

while opcao == 'S':
    lista.append(int(input('Digite um valor: ')))
    opcao = str(input('Deseja continuar? ')).upper().strip()[0]
    cont += 1
lista.sort(reverse=True)
print('Você digitou \033[33m{}\033[m elementos.'.format(cont))
print('Os valores em ordem decrescente são: \033[33m{}\033[m'.format(lista))
if 5 in lista:
    print('O número \033[33m5\033[m está na lista.')
else:
    print('O número \033[33m5\033[m NÃO está na lista.')