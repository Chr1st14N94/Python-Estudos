n1 = float(input('Quantos dias alugados? '))
n2 = float(input('Quantos KM rodados? '))
dia = n1 * 60
km = n2 * 0.15
print(f'O total a pagar é de R$:{dia+km:.2f}')