'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou
não na tela o processo de cálculo do fatorial.'''

def fatorial(numero, show=False):
    """
    Calcula o fatorial de um número.
    :param numero: número
    :param show: (opcional) Se verdadeiro, mostra os números utilizados no cálculo.
    :return: sem retorno
    """
    f = 1
    for c in range(numero, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# PROGRAMA PRINCIPAL
num = int(input("Informe um número para cálculo fatorial: "))
opcao = str(input('Deseja mostrar o cálculo? (S/N): ').strip().upper()[0])
while opcao not in 'SN':
    print('Opção inválida!')
    opcao = str(input('Deseja mostrar o cálculo? (S/N): ').strip().upper()[0])
if opcao == 'S':
    opcao = True
else:
    opcao = False
print(fatorial(num, opcao))


