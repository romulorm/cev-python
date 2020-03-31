'''Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salario = float(input("Informe o salário do funcionário: "))
if salario > 1250:
    percentual = 10/100
else:
    percentual = 15/100
print("O salário do funcionário passará a ser R${:.2f} após o aumento.".format(salario + salario * percentual))