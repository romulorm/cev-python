from urllib import request
from datetime import datetime
from time import sleep


def verificaArquivo(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
        return True
    except FileNotFoundError:
        print('\33[33mArquivo não existe. Criando um novo agora!\33[m')
        try:
            a = open(arquivo, 'wt+')
            a.close()
            return True
        except:
            print('\33[31mAlguma outra falha ocorreu na criação do arquivo!\33[m')
            return False
    except:
        print('\33[31mFalha na verificação do arquivo de dados!\33[m')


def registraLog(s, a):
    status = ''
    horario = datetime.now().replace(microsecond=0)
    try:
        request.urlopen(s)
        status = 'OK'
    except:
        status = 'Problem'
    finally:
        print(f'{status};{horario}')
        arq = open(a, 'a')
        arq.writelines(f'{status};{horario}\n')
        arq.close()


