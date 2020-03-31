'''Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor
da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou
então o empréstimo será negado.'''

print('\033[31m-=-' * 11)
print("SISTEMA DE CÁLCULO DE EMPRÉSTIMO")
print('-=-' * 11)
print('\033[m')
valorImovel = float(input('Insira o valor do imóvel a ser financiado: R$ '))
salario = float(input("Insira o salário do cliente: R$ "))
parcelas = int(input("Insira a quantidade de parcelas: "))
valorParcela = valorImovel / parcelas
print("Para pagar o imóvel de R${:.2f} em {} parcelas a prestação será de R${:.2f} por mês.".format(valorImovel, parcelas, valorParcela))
if valorImovel / parcelas > salario * 0.3:
    print("O empréstimo NÃO pode ser concedido.")
else:
    print("O empréstimo PODE ser concedido.")
