'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

pessoas = list()
pessoa = dict()
opcao = 'S'
somaidade = 0

while opcao == 'S':
    pessoa['nome'] = str(input('Nome: '))
    sex = str(input('Sexo (M/F): ')).upper().strip()[0]
    while sex not in 'MF':
        print('Erro! As opções são: M ou F')
        sex = str(input('Sexo (M/F): ')).upper().strip()[0]
    pessoa['sexo'] = sex
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    somaidade += pessoa['idade']
    opcao = str(input('Deseja continuar? (S/N): ')).upper().strip()[0]
    while opcao not in 'SN':
        print('Erro! As opções são: S ou N')
        opcao = str(input('Deseja continuar? (S/N): ')).upper().strip()[0]
print('A) Ao todo temos {} pessoas cadastradas.'.format(len(pessoas)))
print('B) A média de idade das pessoas é {:.1f}.'.format(somaidade / len(pessoas)))
print('C) As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print('{}'.format(p['nome']), end=', ')
print('')
print('D) Lista das pessoas acima da média de idade:')
for p in pessoas:
    if p['idade'] > (somaidade / len(pessoas)):
        print('      {}'.format(p))