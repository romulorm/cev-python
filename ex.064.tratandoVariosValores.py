num = -1
total = 0
cont = 0
while num != 999:
    num = int(input('Digite um número. [999 para parar]: '))
    if num != 999:
        total += num
        cont +=1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, total))
