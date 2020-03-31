'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de
contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import datetime

trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
age = datetime.now().year - nasc
trabalhador['idade'] = age
trabalhador['ctps'] = int(input('Carteira de Trabalho: (0 para não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('Ano da Contratação: '))
    trabalhador['salario'] = float(input('Salário: R$ '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + (trabalhador['contratacao'] + 35) - datetime.now().year

print('=-=' * 20)
for k, v in trabalhador.items():
    print('\33[31m{}\33[m tem o valor: \33[32m{}\33[m'.format(k, v))
