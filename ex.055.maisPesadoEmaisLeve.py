maisLeve = 1000
maisPesado = 0
for c in range(1, 6):
    peso = float(input("Informe o peso da {}ª pessoa: ".format(c)))
    if c == 1:
        maisPesado = peso
        maisLeve = peso
    else:
        if  peso > maisPesado:
            maisPesado = peso
        if peso < maisLeve:
            maisLeve = peso
    
print("Dos pesos digitados, {}kg foi o maior e {}kg foi o menor.".format(maisPesado, maisLeve))
