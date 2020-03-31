opcao = 'S'
lista = []
while opcao == 'S':
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado! Não vou adicioná-lo...')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso...')
    opcao = str(input('Deseja adicionar outro número? ')).upper().strip()[0]
print('Você digigou os valores: {}'.format(sorted(lista)))