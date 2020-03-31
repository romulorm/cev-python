peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    condicao = "Abaixo do peso"
elif imc <= 25:
    condicao = "Peso ideal"
elif imc <= 30:
    condicao = "Sobrepeso"
elif imc <= 40:
    condicao = "Obesidade"
else:
    condicao = "Obesidade mórbida"
print("O seu IMC é {:.1f}. Condição: {}.".format(imc, condicao)) 
