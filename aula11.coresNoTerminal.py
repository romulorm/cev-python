"""\033[Escape code, this is always the same
Style:
0 - normal, 1 - Bold, 2 - Underline, 3 = Negative1, 5 - Negative2
Text colour: 30 - 37
Background colour: 40 to 47

This table shows some of the available formats;
TEXT COLOR    CODE    TEXT STYLE    CODE    BACKGROUND COLOR    CODE
Black    30    No effect    0    Black    40
Red    31    Bold    1    Red    41
Green    32    Underline    2    Green    42
Yellow    33    Negative1    3    Yellow    43
Blue    34    Negative2    5    Blue    44
Purple    35            Purple    45
Cyan    36            Cyan    46
White    37            White    47

Examples:

print("\033[0;37;40m Normal text \n")
print("\033[0;36;41m Cyan text with red background\033[0;37;40m \n")
print("\033[1;32;40m Bright Bold Green  \n")
print("\033[3;31;40m Italic Red Colour\033[0;37;40m \n")

"""

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

nome = input("Olá, qual o seu nome? ")
print("Muito prazer em te conhecer {}{}{}!!!!!!!".format(cores["amarelo"], nome, cores["limpa"]))