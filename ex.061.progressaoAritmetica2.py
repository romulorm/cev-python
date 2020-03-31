n = int(input("Digite o primeiro termo da P.A.: "))
r = int(input("Digite a razão: "))
c = 1
print("{} ->".format(n),end=' ')
while c < 10:
    n += r
    c += 1
    print("{} ->".format(n),end=' ')
print("ACABOU")