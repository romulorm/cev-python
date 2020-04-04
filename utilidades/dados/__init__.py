def leiaDinheiro(v):
    valido = False
    while not valido:
        entrada = str(input(v)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print('\33[31mERRO: Preço inválido!\33[m'.format(v))
        else:
            valido = True
            return float(entrada)


