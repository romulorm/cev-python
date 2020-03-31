'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''

def notas(*notasalunos, sit=False):
    """
    Função para analisar notas de alunos e situações da turma.
    :param notasalunos: uma ou mais notas de alunos.
    :param sit: (valor opcional). Se True, mostra a situação da turma.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    cont = soma = maior = media = 0
    menor = 999
    turma = dict()
    turma['total'] = len(notasalunos[0])
    for n in notasalunos[0]:
        if int(n) > maior:
            maior = n
            turma['maior'] = maior
        if int(n) < menor:
            menor = n
            turma['menor'] = menor
        cont += 1
        soma += n
        media = soma / cont
        turma['media'] = media
    if str(notasalunos[1]) == 'sit=True':
        if media < 5:
            turma['situacao'] = 'Ruim'
        elif media >= 9:
            turma['situacao'] = 'Ótima'
        else:
            turma['situacao'] = 'Boa'
        return turma
    else:
        return turma


# PROGRAMA PRINCIPAL
l_notas = list()
while True:
    n = float(input('Nota do aluno: '))
    l_notas.append(n)
    opcao = str(input('Deseja continuar? (S/N): ').strip().upper()[0])
    if opcao == 'N':
        break
opcao2 = str(input('Deseja ver a situação da turma com base nos dados? (S/N): ').strip().upper()[0])
if opcao2 == 'S':
    situacao = 'sit=True'
else:
    situacao = 'sit=False'
resp = notas(l_notas, situacao)
print(resp)

help(notas)

