maior = 0
menor = 0
for c in range(1,6):
    n1 = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1

print(f'O maior peso é {maior}\n'
      f'O menor peso é {menor}')