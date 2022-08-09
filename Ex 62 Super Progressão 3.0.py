print('Gerador de PA')
print('-=='* 30)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} \033[1;33m->\033[m '.format(termo), end='')
        termo += razao
        cont += 1
    print('\033[1;31mPausa\033[m')
    print('-=='* 30)
    mais = int(input('Quantos termos você quer a mais?'))
print('Progressão finalizasa com \033[1;34m{}\033[m termos mostrados.'.format(total))
