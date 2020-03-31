sexo = str(input("Por favor informe o seu sexo (M/F): ").upper()[0].strip())
while sexo not in 'MF':
    sexo = str(input('Opção inválida. Por favor, digite corretamente a opção: ').upper()[0].strip())
print('Sexo {} registrado com sucesso!'.format(sexo))