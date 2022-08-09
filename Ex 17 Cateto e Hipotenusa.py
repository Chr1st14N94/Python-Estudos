import math
n1 = float(input('Comprimento do cateto oposto: '))
n2 = float(input('Coprimento do cateto adjacente: '))
hi = (n1 ** 2 + n2 ** 2) ** (1/2)
print(f'A hipotenusa vai medir {math.hypot(n1,n2):.2f}')
print('=-'*10)
print(f'{hi:.2f}')
