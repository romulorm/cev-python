# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

contaMenor = 0
idadeHomemMaisVelho = 0
homemMaisVelho = ''
soma = 0
for c in range(1, 5):
    print("--------- {}ª PESSOA ----------".format(c))
    nome = str(input("Nome: ").strip())
    idade = int(input("Idade: "))
    sexo = str(input("Sexo (M/F): ").upper().strip())
    soma += idade
    if sexo == 'M' and idade > idadeHomemMaisVelho:
        idadeHomemMaisVelho = idade
        homemMaisVelho = nome
    if sexo == "F" and idade < 20:
        contaMenor += 1
print("A média da idade do grupo é de {} anos".format(int(soma / c)))
if idadeHomemMaisVelho != 0:
    print("O homem mais velho tem {} anos e se chama {}.".format(idadeHomemMaisVelho, homemMaisVelho))
print("Ao todo são {} mulheres com menos de 20 anos.".format(contaMenor))
