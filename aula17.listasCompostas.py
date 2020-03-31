galera = [['Romulo', 42], ['Claudia', 44], ['Miguel', 8], ['Raphael', 5]]
for pessoa in galera:
    print('\033[32mNome: {} \033[m'.format(pessoa[0]))
    print('\033[31mIdade: {}\033[m '.format(pessoa[1]))
    if pessoa[1] >= 21:
        print('\033[34m{} é maior de idade.\033[m'.format(pessoa[0]))
    else:
        print('\033[34m{} é menor de idade.\033[m'.format(pessoa[0]))
    print('-=-' * 15)
