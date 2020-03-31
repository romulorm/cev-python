import math

angulo = float(input('Insira um ângulo em graus: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O SENO do ângulo de {}° é {:.2f}'.format(angulo, seno))
print('O COSSENO do ângulo de {}° é {:.2f}'.format(angulo, cosseno))
print('A TANGENTE do ângulo de {}° é {:.2f}'.format(angulo, tangente))


