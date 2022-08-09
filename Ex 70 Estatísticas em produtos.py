print('=-' * 15)
print('SUPER BARATÃO STORE')
print('=-' * 15)
s = maior = menor = cont = 0
barato = ' '
mil = 0
while True:
    prod = str(input('Nome do produto: ')).title()
    valor = float(input('Preço: R$ '))
    s = s + valor
    cont = cont + 1
    if valor > 1000:
       mil = mil + 1
    if cont == 1:
        maior = menor = valor
        barato = prod
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
            barato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break


print(f'O total da compra foi R$:{s:.2f}\n'
      f'Temos {mil} produto custando mais de R$:1000,00\n'
      f'O produto mais barato foi {barato} que custa R$:{menor:.2f}\n'
      f'O produto mais caro custa R$:{maior:.2f}')