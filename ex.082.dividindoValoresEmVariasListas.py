lista = []
listaPar = []
listaImpar = []
opcao = 'S'
while opcao == 'S':
    n = (int(input('Digite um número: ')))
    lista.append(n)
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)
    opcao = str(input('Quer continuar? ').upper().strip()[0])
print('A lista completa é {}'.format(lista))
print('A lista de pares é {}'.format(listaPar))
print('A lista de ímpares é {}'.format(listaImpar))