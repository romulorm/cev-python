exp = str(input('Digite a expressão: '))
abre = exp.count("(")
fecha = exp.count(")")
if abre == fecha:
    print('\033[32mA sua expressão está correta.\033[m')
else:
    print('\033[31mA sua expressão está ERRADA.\033[m')
