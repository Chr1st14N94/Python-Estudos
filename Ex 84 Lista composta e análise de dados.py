dados = []
inf = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(inf) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    inf.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break
print(f'Ao todo temos {len(inf)} pessoas cadastradas.')
print(f'O maior peso foi de {maior}Kg ',end=' ')
for p in inf:
    if p[1] == maior:
        print(f'{p[0]} ',end=' ')
print()
print(f'O menor peso foi de {menor}Kg ', end=' ')
for p in inf:
    if p[1] == menor:
        print(f'{p[0]} ', end=' ')
print()
