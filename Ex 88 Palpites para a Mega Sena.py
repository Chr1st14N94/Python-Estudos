from time import sleep
from random import randint
lista = []
n1 = int(input('Quantos jogos? '))
print('JOGA NA MEGA')
for i in range(n1):
    lista.clear()
    cont = 0
    while True:
        n2 = randint(1, 60)
        if n2 not in lista:
            lista.append(n2)
            cont = cont + 1
        if cont >= 6:
            break
    lista.sort()
    sleep(1)
    print(f'Jogo número {i+1}:',lista)
print('Boa Sorte!')