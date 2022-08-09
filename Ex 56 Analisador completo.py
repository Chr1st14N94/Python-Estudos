s = sf = velho = cont = 0
nome = ' '
for c in range(1,5):
    print(f'----- {c}ª PESSOA -----')
    n1 = str(input('Nome: '))
    n2 = int(input('Idade: '))
    n3 = str(input('Sexo [M/F]: ')).upper()[0]
    s = s + n2
    if n3 == 'M':
        if n2 > velho:
            velho = n2
            nome = n1
    if n3 == 'F':
        if n2 < 19:
            sf = sf + 1

print(f'A média de idade do grupo é de {s / 4:.1f} anos.\n'
      f'O homem mais velho tem {velho} anos e se chama {nome}.\n'
      f'Ao todo são {sf} mulher(es) com menos de 20 anos.')