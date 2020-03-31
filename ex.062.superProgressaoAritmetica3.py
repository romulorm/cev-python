n = int(input("Digite o primeiro termo da P.A.: "))
r = int(input("Digite a razão: "))
c = 1
print("{} ->".format(n), end=' ')
while c < 10:
    n += r
    c += 1
    print("{} ->".format(n), end=' ')
print("PAUSA")
opcao = -1
while opcao != 0:
    opcao = int(input("Quantos termos vc quer mostrar a mais? "))
    d = c + opcao
    while c < d:
        n += r
        c += 1
        print("{} ->".format(n), end=' ')
    print("PAUSA")
print("\033[32mProgressão finalizada com {} termos.".format(c))
