n1 = int(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {n1:.2f}Km.\n')
if n1 <= 200:
    n2 = (n1 * 0.50)
else:
    n2 = (n1 * 0.45)
print(f'E o preço da sua passagem será de R$:{n2:.2f}')
