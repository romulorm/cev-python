print('-=-' * 13)
print('-=- Estatísticas - Brasileirão 2019 -=-')
print('-=-' * 13)

bra2019 = ('Flamengo','Santos','Palmeiras','Grêmio','Atlético-PR',
           'São Paulo','Internacional','Corinthians','Fortaleza',
           'Goiás','Bahia','Vasco','Atlético-MG','Fluminense','Botafogo',
           'Ceará','Cruzeiro','CSA','Chapecoense','Avaí')
print('\033[32mLista de times do Brasileirão 2019 por colocação:\033[m \n{}'.format(bra2019))
print('\033[32mLista dos 5 primeiros colocados do Brasileirão 2019:\033[m \n{}'.format(bra2019[:5]))
print('\033[32mLista dos 4 últimos colocados do Brasileirão 2019:\033[m \n{}'.format(bra2019[-4:]))
print('\033[32mLista de times do Brasileirão 2019 em ordem alfabética:\033[m \n{}'.format(sorted(bra2019)))
print('\033[32mPosição do Chapecoense no Brasileirão 2019:\033[m \n{}º'.format(bra2019.index('Chapecoense') + 1))
