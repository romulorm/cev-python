import time

maior = 0
opcao = 11
n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))
while opcao not in [12345]:
    print('''Opções disponíveis:
             (1) Somar
             (2) Multiplicar
             (3) Maior
             (4) Novos números
             (5) Sair''')
    opcao = int(input("Escolha uma opção acima: "))
    if opcao == 1:
        print("\033[34mA soma entre {} e {} é: \033[32m{}\033[m".format(n1, n2, n1 + n2))
    elif opcao == 2:
        print("\033[34mA multiplicação entre {} e {} é: \033[32m{}\033[m".format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("\033[34mO maior número entre {} e {} é: \033[32m{}\033[m".format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input("Informe um número: "))
        n2 = int(input("Informe outro número: "))
    if opcao == 5:
        print("\033[32mFinalizando o programa...")
        time.sleep(1)
        print("\033[31mVolte sempre!!")
        exit(0)
