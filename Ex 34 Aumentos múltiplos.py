n1 = float(input('Salário do funcionário: '))
if n1 <= 1250:
    aumento = n1 * 15 / 100
    por = '15%'
else:
    aumento = n1 * 10 / 100
    por = '10%'
print(f'O salário do funcionário era R$:{n1:.2f}, '
      f'com o aumento de {por} R$:{aumento:.2f},\n'
      f'o funcionário passará a ganhar R$:{n1+aumento:.2f}')