lista = []
imp = []
par = []
while True:
    n1 = int(input('Digite um número: '))
    lista.append(n1)
    if n1 % 2 == 0:
        par.append(n1)
    else:
        imp.append(n1)
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break
print(f'A lista completa é {sorted(lista)}\n'
      f'A lista de pares é {sorted(par)}\n'
      f'A lista de impares é {sorted(imp)}')