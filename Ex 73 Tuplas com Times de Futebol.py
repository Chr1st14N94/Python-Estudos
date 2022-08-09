times = ('Atlético-MG','Flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino',
        'Fluminense','América-MG','Atlético-GO','Santos','Ceará','Internacional',
        'São Paulo','Athletico-PR','Cuiabá','Juventude','Grêmio','Bahia','Sport','Chapecoense')
print(f'Lista do Brasileirão: {times}')
print(f'Os times na ordem alfabética são {sorted(times)}')
print(f'Os 5 primeiros são {times[:5]}')
print(f'Os 4 últimos são {times[-4:]}')
print(f'O CHAPECOENSE está na {times.index("Chapecoense")+1}ª posição.')