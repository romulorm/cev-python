from random import randint

numCPU = randint(1, 5)
print("-=-" * 18)
print("Vou pensar em um número de 1 a 5. Tente adivinhá-lo.")
print("-=-" * 18)
numHUMAN = int(input("Em que número eu pensei? "))
print("\033[32mParabéns, você acertou!, eu pensei no número {}".format(numCPU) if numCPU == numHUMAN else "\033[31mVocê errou. Eu pensei no número {}. Tente outra vez!".format(numCPU))
