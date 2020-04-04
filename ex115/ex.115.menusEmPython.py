from ex115.menu import *
from ex115.arquivo import *

arq = 'database.txt'

if not arquivoExiste(arq):
    criaArquivo(arq)

while True:
    resposta = siscad(['Pessoas cadastradas', 'Cadastrar pessoas', 'Finalizar programa'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('Cadastrar pessoa')
        name = str(input('Nome: '))
        age = leiaInt('Idade: ')
        cadastrarPessoa(arq, name, age)
    elif resposta == 3:
        print('\33[31mFinalizando programa! Até logo!\33[m')
        break
    else:
        print('\33[31mOpção inválida!\33[m')



