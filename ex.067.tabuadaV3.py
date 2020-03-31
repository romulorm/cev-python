num = 1
while True:
    cont = opcao = result = 0
    print('-' * 20)
    num = int(input('Quer ver a tabuada de qual número? (negativo para sair): '))
    print('-' * 20)
    if num < 0:
        break
    else:
        while cont <10:
            cont +=1
            result = num * cont
            print('{} x {} = {}'.format(num, cont, result))
print('\033[31mPrograma Tabuada 3.0 encerrado. Volte sempre!')
