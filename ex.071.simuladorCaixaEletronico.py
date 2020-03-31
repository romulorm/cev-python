print('-=-' * 9)
print('  \033[35m--- BANCO GUANABARA ---\033[m ')
print('-=-' * 9)
valor = int(input('Qual valor você quer sacar? (Cédulas disponíveis: 100, 50, 20 e 10): '))
for nota in [100, 50, 20, 10]:
    qtde = valor // nota
    valor = valor % nota
    if qtde > 0:
        print('Cédulas de R$ {},00: \033[33m{}\033[m'.format(nota, qtde))

'''qtde100 = qtde50 = qtde20 = qtde10 = 0
valor = 1
print('-=-' * 9)
print('  \033[35m--- BANCO GUANABARA ---\033[m ')
print('-=-' * 9)
while valor % 10 != 0:
    valor = int(input('Qual valor você quer sacar? (Cédulas disponíveis: 100, 50, 20 e 10): '))
while valor >= 100:
    qtde100 += 1
    valor -= 100
while valor >= 50:
    qtde50 += 1
    valor -= 50
while valor >= 20:
    qtde20 += 1
    valor -= 20
while valor >= 10:
    qtde10 += 1
    valor -= 10
if qtde100 > 0:
    print('Cédulas de R$100,00: \033[31m{}\033[m'.format(int(qtde100)))
if qtde50 > 0:
    print('Cédulas de R$50,00: \033[32m{}\033[m'.format(int(qtde50)))
if qtde20 > 0:
    print('Cédulas de R$20,00: \033[33m{}\033[m'.format(int(qtde20)))
if qtde10 > 0:
    print('Cédulas de R$10,00: \033[34m{}\033[m'.format(int(qtde10)))
print('\033[35mVolte sempre ao Banco Guanabara! Tenha um bom dia!')'''
