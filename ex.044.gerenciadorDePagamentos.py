"""Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço
normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros"""

print("-=-" * 15)
print("  \033[36m============ LOJAS GUANABARA ============\033[m")
print("-=-" * 15)

valorCompras = float(input("Informe o total das compras (R$): "))
print("-=-" * 15)
print('''Escolha uma das opções abaixo: 
(1) à vista dinheiro/cheque - 10% desconto
(2) à vista no cartão - 5% desconto
(3) em 2 vezes no cartão
(4) 3 a 10 vezes no cartão - 20% de acréscimo
---------------------------------------------''')
opcao = int(input("Informe a opção: "))

if opcao == 1:
    totalpagar = valorCompras * 0.9
elif opcao == 2:
    totalpagar = valorCompras * 0.95
elif opcao == 3:
    qtdeParcelas = 2
    totalpagar = valorCompras
    parcela = totalpagar / 2
    print("-=-" * 15)
    print("\033[34mPagamento em {} parcelas de R$: {:.2f}".format(qtdeParcelas, parcela))
elif opcao == 4:
    qtdeParcelas = int(input("Digite a quantidade de parcelas (3 a 10): "))
    totalpagar = valorCompras * 1.2
    parcela = totalpagar / qtdeParcelas
    print("-=-" * 15)
    print("\033[34mPagamento em {} parcelas de R$ {:.2f}".format(qtdeParcelas, parcela))
else:
    print("\033[31mOpção inválida!! Tente novamente.")
    exit(0)
print("\033[33mTotal a pagar: {:.2f}".format(totalpagar))
