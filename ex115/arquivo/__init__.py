from ex115.menu import cabecalho
from time import sleep

def arquivoExiste(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaArquivo(arquivo):
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquuivo')
    else:
        print('Arquivo criado com sucesso!')


def lerArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
    except FileNotFoundError:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('\33[36mPessoas cadastradas\33[m')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print('{:<30}{:3>} anos'.format(dado[0], dado[1]))
    finally:
        a.close()


def cadastrarPessoa(arquivo, nome, idade):
    try:
        a = open(arquivo, "a")
    except FileNotFoundError:
        print('Erro ao cadastrar a pessoa!')
    else:
        a.writelines(f'{nome};{idade}\n')
        print('\33[33mPessoa cadastrada com sucesso!\33[m')
        sleep(1)
    finally:
        a.close()

