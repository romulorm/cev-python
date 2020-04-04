from ex115.menu import cabecalho

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
        cabecalho('\33[36mPessoas cadastradas\33[m', 30)
        print('\33[35m{}\33[m'.format(a.read()))


def cadastrarPessoa(arquivo, nome, idade):
    try:
        a = open(arquivo, "a")
    except FileNotFoundError:
        print('Erro ao cadastrar a pessoa!')
    else:
        a.writelines(f'{nome};{idade}\n')
        a.close()

