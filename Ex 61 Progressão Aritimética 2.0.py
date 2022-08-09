print('Gerador de PA')
print('-=='* 30)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} \033[1;33m->\033[m '.format(termo), end='')
    termo += razao
    cont += 1
print('\033[1;31mFIM\033[m')
print('-=='* 30)