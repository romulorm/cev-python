import datetime

contMaior = 0
contMenor = 0
for c in range(1, 8):
    age = int(input("Informe o ano de nascimento da {}°	 pessoa.".format(c)))
    anoAtual = datetime.date.today().year
    if  anoAtual - age > 18:
        contMaior += 1
    else:
        contMenor += 1
print("Ao todo tivemos {} pessoas maiores de idade.\nE também tivemos {} pessoas menores de idade.".format(contMaior, contMenor))
