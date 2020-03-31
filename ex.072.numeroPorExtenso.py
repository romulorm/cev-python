extenso = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez')
numero = 999
while numero not in range(0, 11):
    numero = int(input('Digite um número entre 0 e 10: '))
print('Você digitou o número: \33[32m{}\33[m'.format(extenso[numero]))
print('Programa finalizado!')
