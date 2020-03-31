import datetime

datetime.date
anoAtual = datetime.datetime.now()
ano = int(input("Informe o ano a ser analisado. Clique 0 para o ano atual: "))
print("Analisando se o ano é bissexto...")
if ano == 0:
    ano = anoAtual.year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é Bissexto!".format(ano))
else:
    print("O ano {} NÃO é Bissexto!".format(ano))
