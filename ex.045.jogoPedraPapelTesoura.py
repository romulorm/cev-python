# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import choice

print('''Suas opções: 
(1) Pedra
(2) Papel
(3) Tesoura''')

opcao = int(input("Qual a opção desejada? "))
opcaoCpu = choice(['Pedra', 'Papel', 'Tesoura'])

if opcao not in [1, 2, 3]:
    print("\033[31mOpção inválida! Tente novamente!")
    exit(0)
else:
    print("\033[35mJO")
    sleep(1)
    print("\033[36mKEN")
    sleep(1)
    print("\033[34mPO!")
    sleep(1)
    if opcao == 1 and opcaoCpu == 'Tesoura' or opcao == 2 and opcaoCpu == 'Pedra' or opcao == 3 and opcaoCpu == 'Papel':
        print("\033[mA opção escolhida pelo computador foi \033[35m{}".format(opcaoCpu))
        print("\033[32mParabéns!, VOCÊ venceu!")
    elif opcao == 1 and opcaoCpu == 'Papel' or opcao == 2 and opcaoCpu == 'Tesoura' or opcao == 3 and opcaoCpu == 'Pedra':
        print("\033[mA opção escolhida pelo computador foi \033[35m{}".format(opcaoCpu))
        print("\033[31mO COMPUTADOR venceu! Tente novamente!")
    else:
        print("\033[mA opção escolhida pelo computador foi \033[35m{}".format(opcaoCpu))
        print("\033[33mVocê empatou com o computador.")
