jogador = dict()
time = list()
gols = list()
total = numGols = 0

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input('Quantas partidas {} jogou? '.format(jogador['nome'])))
    for g in range(1, jogador['partidas'] + 1):
        numGols = int(input('Quantos gols na partida {}? '.format(g)))
        total += numGols
        gols.append(numGols)
    jogador['gols'] = gols[:]
    jogador['total'] = total
    gols.clear()
    total = 0
    time.append(jogador.copy())
    opcao = str(input('Cadastrar novo jogador? (S/N) ').upper().strip()[0])
    if opcao == 'N':
        break
print('\33[32m{:<5}{:<20}{:<20}{:<5}\33[m'.format('cod', 'nome', 'gols', 'total'))
print('=-=' * 17)
for k, v in enumerate(time):
    print('{:<5}{:<20}{:<20}{:<5}'.format(k, v['nome'], str(v['gols']), v['total']))
while True:
    resp = int(input('Mostrar dados de qual jogador? 999 para finalizar. '))
    print('=-=' * 16)
    if resp == 999:
        print('\33[31mPrograma finalizado. Volte sempre!\33[m')
        break
    elif len(time) > resp:
        for k, v in enumerate(time):
            if resp == k:
                print('Levantamento do jogador: \33[33m{}\33[m'.format(v['nome']))
                for i, g in enumerate(v['gols']):
                    print('No jogo {} fez {} gols.'.format(i + 1, g))
    else:
        print('Opção inválida!')
