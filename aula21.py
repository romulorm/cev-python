def somar(a, b, c):
    s = a + b + c
    return s


def fatorial(n):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f

# Programa Principal

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite o último número: '))
print('A soma dos números é {}'.format(somar(n1, n2, n3)))

f1 = int(input('Digite um número: '))
print('O fatorial de {} é {}'.format(f1, fatorial(f1)))
