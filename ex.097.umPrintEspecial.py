'''Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
parâmetro e mostre uma mensagem com tamanho adaptável.'''

def escreva(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))


texto = str(input('Escreva uma frase longa: '))
escreva(texto)
texto = str(input('Escreva uma frase curta: '))
escreva(texto)

