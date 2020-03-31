import math

ca = float(input('Digite o valor do Cateto Adjacente: '))
co = float(input('Digite o valor do Cateto Oposto: '))
hi = math.hypot(ca, co)
print('O valor da hipotenusa é: {:.2f}'.format(hi))

