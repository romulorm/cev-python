n = int(input("Digite o primeiro termo da P.A.: "))
r = int(input("Digite a razão: "))
print("{} ->".format(n),end=' ')
for c in range(1, 10):
    n += r
    print("{} ->".format(n),end=' ')
print("ACABOU")