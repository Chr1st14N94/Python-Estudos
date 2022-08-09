menu = 'S'
s = c = 0
maior = menor = 0
while menu == 'S':
    n1 = int(input('Digite um número: '))
    op = str(input('Quer continuar? [S/N] ')).upper()[0]
    if op not in 'SN':
        print('Obção inválida, tente novamente!')
    if op == 'N':
        menu = 'N'
    s = s + n1
    c = c + 1
    if c == 1:
        maior = n1
        menor = n1
    elif c > 1:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1


print(f'Você digitou {c} números e a média foi {s / c:.2f}\n'
      f'O maior valor foi {maior} e o menor foi {menor}')