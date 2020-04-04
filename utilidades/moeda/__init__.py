def aumentar(valor, taxa, formato=False):
    result = valor + (valor * taxa / 100)
    return result if not formato else formatar(result)


def diminuir(valor, taxa, formato=False):
    result = valor - (valor * taxa / 100)
    return result if not formato else formatar(result)


def dobro(valor, formato=False):
    result = valor * 2
    return result if not formato else formatar(result)


def metade(valor, formato=False):
    result = valor / 2
    return result if not formato else formatar(result)


def formatar(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')

def resumo (valor, taxaac=10, taxared=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{formatar(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'Aumento de {taxaac}%: \t{aumentar(valor, 20, True)}')
    print(f'Redução de {taxared}%: \t{diminuir(valor, 10, True)}')
    print('-' * 30)