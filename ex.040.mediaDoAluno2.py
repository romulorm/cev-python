'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
 no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''


nome = input('Escreva o nome do aluno: ')
nota1 = float(input('Escreva a primeira nota do aluno: '))
nota2 = float(input('Escreva a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print('-' * 40)
print('Notas do aluno: {}'.format(nome))
print('-' * 40)
print('Nota 1 = {}'.format(nota1))
print('Nota 2 = {}'.format(nota2))
print('Média do aluno: {}'.format(media))
if media < 5:
    print("Aluno REPROVADO.")
elif media > 5 and media < 6.9:
    print("Aluno em RECUPERAÇÃO.")
else:
    print("Aluno APROVADO!")