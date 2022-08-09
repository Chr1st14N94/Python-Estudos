soccer = dict()
gols = []
soccer['nome'] = str(input('Nome do jogador: ')).title()
part = int(input(f'Quantas partidas {soccer["nome"]} jogou? '))
for c in range(part):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
soccer['gols'] = gols
soccer['total'] = sum(gols)
print('=-' * 27)
print(soccer)
print('=-' * 27)
for i,v in soccer.items():
    print(f'O campo {i} tem o valor {v}')
print('=-' * 27)
print(f'O jogador {soccer["nome"]} jogou {part} partidas.')
for k,l in enumerate(soccer['gols']):
    print(f'   => Na partida {k+1}, fez {l} gols.')
print()
print(f'Foi um total de {soccer["total"]} gols')
