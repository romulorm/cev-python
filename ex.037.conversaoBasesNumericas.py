'''Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

print('-=-' * 11)
print('Conversor de bases numéricas')
print('-=-' * 11)
numero = int(input("Insira um número inteiro: "))
print('''Escolha uma das opções para a conversão:
(1) para BINÁRIO
(2) para OCTAL
(3) para HEXADECIMAL''')
opcao = int(input("Sua opção: "))
if opcao == 1:
    print("O número decimal {} equivale a {} em BINÁRIO.".format(numero, str(bin(numero)).strip("0b")))
elif opcao == 2:
    print("O número decimal {} equivale a {} em OCTAL".format(numero, str(oct(numero)).strip("0o")))
elif opcao == 3:
    print("O número decimal {} equivale a {} em HEXADECIMAL.".format(numero, str(hex(numero).strip("0x"))))
else:
    print("Opção inválida!! Tente novamente.")
