from datetime import date
hoje = date.today().year
velho = novo = 0

for c in range(1,7):
    n1 = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = hoje - n1
    if idade > 17:
        velho = velho + 1
    else:
        novo = novo + 1
print(f'Ao todo {velho} pessoas maiores de idade,\n'
      f'E também tivemos {novo} pessoas menores de idade.')