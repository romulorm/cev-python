'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função
 input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''

def leiaInt(msg):
    n = str(input(msg))
    while not n.isnumeric():
        print('\33[31mDigite um número inteiro válido!\33[m')
        n = str(input(msg))
    return n


# PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print('Você acabou de digitar o número {}.'.format(n))