import random

aluno1 = input('Insira o nome do primeiro aluno: ')
aluno2 = input('Insira o nome do segundo aluno: ')
aluno3 = input('Insira o nome do terceiro aluno: ')
aluno4 = input('Insira o nome do quarto aluno: ')
alunoSorteado = random.choice([aluno1, aluno2, aluno3, aluno4])
print('O aluno sorteado foi: {}'.format(alunoSorteado))


