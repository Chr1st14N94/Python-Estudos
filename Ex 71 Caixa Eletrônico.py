duz = cem = cin = vin = dez = cinc = doi = um = 0
n1 = int(input('Que valor você quer sacar? '))
while n1 >= 200:
    duz = duz + 1
    n1 = n1 - 200
if duz != 0:
    print(f'Total de {duz} cédulas de R$:200')
while n1 >= 100:
    cem = cem + 1
    n1 = n1 - 100
if cem != 0:
    print(f'Total de {cem} cédulas de R$:100')
while n1 >= 50:
    cin = cin + 1
    n1 = n1 - 50
if cin != 0:
    print(f'Total de {cin} cédulas de R$:50')
while n1 >= 20:
    vin = vin + 1
    n1 = n1 - 20
if vin != 0:
    print(f'Total de {vin} cédulas de R$:20')
while n1 >= 10:
    dez = dez + 1
    n1 = n1 - 10
if dez != 0:
    print(f'Total de {dez} cédulas de R$:10')
while n1 >= 5:
    cinc = cinc + 1
    n1 = n1 - 5
if cinc != 0:
    print(f'Total de {cinc} cédulas de R$:5')
while n1 >= 2:
    doi = doi + 1
    n1 = n1 - 2
if doi != 0:
    print(f'Total de {doi} cédulas de R$:2')
while n1 >= 1:
    um = um + 1
    n1 = n1 - 1
if um != 0:
    print(f'E uma moeda de R$:1')
