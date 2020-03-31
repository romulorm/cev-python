qtdeMulher20 = qtdeM18 = qtdeH = 0

while True:
    print('-=-' * 12)
    idade = int(input('Idade: '))
    if idade > 18:
        qtdeM18 +=1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ').upper().strip()[0])
        print('-=-' * 12)
    if sexo == 'M':
        qtdeH += 1
    else:
        if idade < 18:
            qtdeMulher20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('\033[31mQuer continuar?\033[m ').upper().strip()[0])
    if resp == 'N':
        break
print('\033[34mTotal de pessoas com mais de 18 anos: {}'.format(qtdeM18))
print('\033[32mAo todo temos {} homens cadastrados.'.format(qtdeH))
print('\033[33mE temos {} mulheres com menos de 20 anos.'.format(qtdeMulher20))