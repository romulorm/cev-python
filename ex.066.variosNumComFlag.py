soma = num = cont = 0
while True:
    num = int(input('Digite um número. (999 para parar): '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print('A soma dos {} valores foi {}.'.format(cont, soma))
