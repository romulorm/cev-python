div = 0
n = int(input("Digite um número: "))
for c in range(1, n + 1):
    if n % c == 0:
        print("\033[32m{}\033[m".format(c),end=' ')
        div += 1
    else:
        print("\033[31m{}\033[m".format(c),end=' ')

print("\nO número {} foi divísível {} vezes.".format(n, div))
if div == 2:
    print("Então ele é PRIMO.")
else:
    print("Então ele NÃO é PRIMO.")