num = int(input("Digite um número para gerar a tabuada: "))
print("-=-" * 5)
print("Tabuada de {}".format(num))
print("-=-" * 5)
for a in range(1, 11):
    print("{} x {} = {}".format(num, a, num * a))
