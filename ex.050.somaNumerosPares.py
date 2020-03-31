soma = 0
cont = 0
for c in range(1, 7):
    n = int(input("Digite o {}º número: ".format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print("Vocẽ informou {} números PARES e a soma deles foi {}.".format(cont, soma))