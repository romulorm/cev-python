from random import randint

numCPU = randint(1, 10)
print("-=-" * 18)
print("Sou o seu computador. Vou pensar em um número de 1 a 10. Tente adivinhá-lo.")
print("-=-" * 18)
numHUMAN = int(input("Em que número eu pensei? "))
contador = 1
while numHUMAN != numCPU:
    if numCPU > numHUMAN:
        print('meu número é MAIOR. Tente novamente...')
    else:
        print('O meu número é MENOR. Tente novamente...')
    numHUMAN = int(input('Qual o seu palpite? '))
    contador += 1
print("\033[32mParabéns, você acertou, mas utilizou {} tentativas.".format(contador))
