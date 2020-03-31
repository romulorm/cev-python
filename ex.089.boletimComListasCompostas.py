'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
 composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente.'''

aluno = list()
classe = list()
opcao = 'S'

print('-=-' * 12)
print('--- GERÊNCIA ACADÊMICA ---')
print('-=-' * 12)
while opcao == 'S':
    nome = str(input('Nome do aluno: '))
    aluno.append(nome)
    nota1 = float(input('Primeira nota do aluno: '))
    aluno.append(nota1)
    nota2 = float(input('Segunda nota do aluno: '))
    aluno.append(nota2)
    classe.append(aluno[:])
    aluno.clear()
    opcao = str(input('Deseja continuar? ').strip().upper()[0])
print(f'\33[32m{"Nº":<4}{"ALUNO":<25}{"MÉDIA":>4}\33[m')
for i, al in enumerate(classe):
    print('\33[31m{:<4}{:<25}{:<4.1f}\33[m'.format(i, al[0], (al[1] + al[2]) / 2))

numeroAluno = 0
while True:
    numeroAluno = int(input('Deseja mostrar as notas de qual aluno? [999 para finalizar] '))
    if numeroAluno == 999:
        break
    if numeroAluno <= len(classe) - 1:
        print('As notas do aluno {} são: {} e {}'.format(classe[numeroAluno][0], classe[numeroAluno][1], classe[numeroAluno][2]))
print('Programa finalizado!')
