from random import randint


def sorteia(lista):
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(1, 6):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
    print('PRONTO!')


def somapar(lista):
    som = 0
    for i in lista:
        if i % 2 == 0:
            som += i
    print(f'Somando os valores pares de {lista}, temos {som}')


numeros = list()
sorteia(numeros)
somapar(numeros)