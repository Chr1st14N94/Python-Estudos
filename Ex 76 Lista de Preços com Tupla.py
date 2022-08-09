prod = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
        'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 180.50, 'Canetas', 28.90, 'Livro', 79.25)
print('\033[1;34m=\033[m'*40)
print(f'\033[1;31m{"LISTAGEM DE PREÇOS":^40}\033[m')
print('\033[1;34m=\033[m'*40)
for pos in range(0,len(prod)):
    if pos % 2 == 0:
        print(f'{prod[pos]:.<30}',end='')
    else:
        print(f'R$:{prod[pos]:>7.2f}')
print('\033[1;34m=\033[m'*40)