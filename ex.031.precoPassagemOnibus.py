# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Qual a distância da viagem, em quilômetros? "))
preco = distancia * 0.45 if distancia > 200 else distancia * 0.50
print("Você vai pagar R$ {:.2f} por uma viagem de {} quilômetros.".format(preco, int(distancia)))
