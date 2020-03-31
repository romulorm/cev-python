"""Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""

print("-=-" * 25)
print("Analisador de Triângulos")
print("-=-" * 25)
r1 = float(input("Informe o primeiro segmento: "))
r2 = float(input("Informe o segundo segmento: "))
r3 = float(input("Informe o terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM formar um triângulo!")
    if r1 == r2 == r3:
        print("O triângulo formado será um EQUILÁTERO!")
    elif r1 != r2 != r3 != r1:
        print("O triângulo formado será um ESCALENO!")
    else:
        print("O triângulo formado será um ISÓSCELES!")
else:
    print("Os segmentos acima NÃO PODEM formar um triângulo!")

