def linha(tamanho=40 ):
    return '-' * tamanho


def cabecalho(txt, tam=40):
    print(linha())
    print(txt.center(tam))
    print(linha())


def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except(TypeError, ValueError):
            print('\33[31mOpção inválida!\33[m')
            continue
        else:
            return n


def siscad(lista):
    cabecalho('\33[32mSISTEMA DE CADASTRO DE PESSOAS\33[m')
    cont = 1
    for item in lista:
        print('{} - {}'.format(cont, item))
        cont += 1
    print(linha())
    opcao = leiaInt('Sua opção: ')
    return opcao

