'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um
 dicionário. No final, mostre o conteúdo da estrutura na tela.'''

ficha = {}
ficha['nome'] = str(input('Nome do aluno: '))
ficha['media'] = float(input('Média do aluno: '))
if ficha['media'] > 6:
    ficha['situacao'] = 'aprovado'
elif ficha['media'] >= 5:
    ficha['situacao'] = 'recuperação'
else:
    ficha['situacao'] = 'reprovado'
print('-=-' * 20)
for k, v in ficha.items():
    print('{} é igual a {}'.format(k, v))