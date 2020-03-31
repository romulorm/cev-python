'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
 nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO
 nas eleições.'''

def verificaEleitor(nasc):
    from datetime import datetime
    anoatual = datetime.now().year
    idade = anoatual - nasc
    if idade < 16:
        return f'Com {idade} anos: \33[31mNÃO VOTA\33[m'
    elif 18 <= idade <= 64:
        return f'Com {idade} anos o voto é \33[32mOBRIGATÓRIO\33[m'
    else:
        return f'Com {idade} anos o voto é \33[33mOPCIONAL\33[m'


# PROGRAMA PRINCIAL

while True:
    anonasc = int(input('Informe o seu ano de nascimento: '))
    print(verificaEleitor(anonasc))
    opcao = str(input('Deseja continuar? (S/N): ').strip().upper()[0])
    while opcao not in 'SN':
        print('\33[31mInforme uma opção válida!\33[m')
        opcao = str(input('Deseja continuar? (S/N): ').strip().upper()[0])
    if opcao == 'N':
        break

