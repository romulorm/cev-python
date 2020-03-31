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
    turma['total'] = len(notasalunos)
    for n in notasalunos:
        if n > maior:
            maior = n
            turma['maior'] = maior
        if n < menor:
            menor = n
            turma['menor'] = menor
        cont += 1
        soma += n
        media = soma / cont
        turma['media'] = media
    if sit:
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
resp = notas(7, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)

