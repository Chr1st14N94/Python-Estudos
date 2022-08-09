from time import sleep
from random import randint
from operator import itemgetter
jogador = {'Jogador1': randint(1, 6),
           'Jogador2': randint(1, 6),
           'Jogador3': randint(1, 6),
           'Jogador4': randint(1, 6)}
ranking = []
for c,i in jogador.items():
    print(f'{c} tirou {i} no dado.')
    sleep(1)
print('RANKING DOS JOGADORES')
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for k,v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
