def linha(tamanho=30 ):
    print('-' * tamanho)

def valida(opcao):
    print('Digite a opção:\n'
          '1) Ver pessoas cadastrados\n'
          '2) Cadastrar pessoas\n'
          '3) Finalizar programa')
    opcao = (input())
    while opcao not in '123':
        print('Opção inválida!')
    if opcao == 1: