frase = str(input("Digite uma frase: ")).upper()
txt = frase.replace(' ', '')
txtInv = txt[::-1]
if txt == txtInv:
    print("O texto é um PALÍNDROMO.")
    print("{} é igual a {}".format(txt, txtInv))
else:
    print("O texto NÃO é um PALÍNDROMO.")
    print("{} é diferente de {}".format(txt, txtInv))
