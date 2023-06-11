from random import randint


def sompar(*num):
    lista = list()
    som = 0
    print('Sorteando 5 valores da lista:', end=' ')
    for c in num:
        print(f'{c}', end=' ')
        lista.append(c)
        if c % 2 == 0:
            som += c
    print('PRONTO!')
    print(f'Somando os valores pares de {lista}, temos {som}')

sompar(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))