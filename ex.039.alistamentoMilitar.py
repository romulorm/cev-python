'''Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
 se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
import datetime

anoNasc = int(input("Digite o ano do seu nascimento: "))
anoAtual = datetime.datetime.now().year
anoAlistamento = anoNasc + 18
if anoAtual == anoAlistamento:
    print("Aliste-se IMEDIATAMENTE")
elif anoAtual < anoAlistamento:
    print("Seu alistamento será no ano de {}".format(anoAlistamento))
else:
    print("Seu alistamento ocorreu no ano de {}".format(anoAlistamento))
