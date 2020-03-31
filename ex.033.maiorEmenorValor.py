val1 = int(input("Insira o primeiro valor inteiro: "))
val2 = int(input("Insira o segundo valor inteiro: "))
val3 = int(input("Insira o terceiro valor inteiro: "))
if val1 > val2:
    maior = val1
    menor = val2
else:
    maior = val2
    menor = val1
if val3 > maior:
    maior = val3
else:
    menor = val3
print("O maior número é: {}".format(maior))
print("O menor número é: {}".format(menor))