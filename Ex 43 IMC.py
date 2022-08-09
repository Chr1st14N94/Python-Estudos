n1 = float(input('Altura: '))
n2 = float(input('Peso: '))
imc = n2 / (n1 *n1)

if imc < 18.5:
    res = 'ABAIXO DO PESO'
    res2 = 'Fique em alerta'
elif 18.5 <= imc < 25:
    res = 'PESO IDEAL'
    res2 = 'PARABÉNS'
elif 25 <= imc < 30:
    res = 'com SOBRE PESO'
    res2 = 'Fique em alerta'
elif 30 <= imc < 40:
    res = 'com OBESIDADE'
    res2 = 'Fique em alerta'
else:
    res = 'com OBESIDADE MÓRBIDA'
    res2 = 'CUIDADO!'
print(f'Seu IMC é de {imc:.1f}\n'
      f'{res2}, você está {res}.')