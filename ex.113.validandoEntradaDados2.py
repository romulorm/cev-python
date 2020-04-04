'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[31mDigite um número inteiro válido!\33[m')
            continue
        except KeyboardInterrupt:
            print('\33[31mEntrada de dados interrompida pelo usuário!\33[m')
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\33[31mDigite um número real válido!\33[m')
            continue
        except KeyboardInterrupt:
            print('\33[31mEntrada de dados interrompida pelo usuário!\33[m')
        else:
            return n


# PROGRAMA PRINCIPAL
n = leiaInt('Digite um número inteiro: ')
print('Você acabou de digitar o número {}.'.format(n))

n = leiaFloat('Digite um número de ponto flutuante: ')
print('Você acabou de digitar o número {}.'.format(n))
