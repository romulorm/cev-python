def linha(tamanho=40 ):
    return '-' * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def leiaInt(num):
    try:
        int(num)
    except(TypeError, ValueError):
        print('Digite uma opção válida!')
    else:
        return num


def siscad(lista):
    cabecalho('SISTEMA DE CADASTRO DE PESSOAS')
    cont = 1
    for item in lista:
        print('{} - {}'.format(cont, item))
        cont += 1
    opcao = leiaInt('Sua opção: ')
    print(linha())

