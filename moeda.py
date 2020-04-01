def aumentar(valor, taxa):
    result = valor + (valor * taxa / 100)
    return result


def diminuir(valor, taxa):
    result = valor - (valor * taxa / 100)
    return result


def dobro(valor):
    result = valor * 2
    return result


def metade(valor):
    result = valor / 2
    return result


def formatar(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')
