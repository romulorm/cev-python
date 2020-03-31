moeda = (input('Escreva o nome da moeda: '))
cotacao = float(input('Digite a cotação da moeda: '))
reais = float(input('Digite a quantidade de reais: '))
total = reais / cotacao
print('{:.2f} reais equivale a {:.2f} em {}'.format(reais, total, moeda))