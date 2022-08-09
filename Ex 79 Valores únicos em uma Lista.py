n1 = []
while True:
    n2 = int(input('Digite um valor: '))
    if n2 not in n1:
        n1.append(n2)
    else:
        print('Número repetido, tente novamente!')
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp in 'Nn':
        break
print(f'{sorted(n1)}')