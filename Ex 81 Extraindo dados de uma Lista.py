lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break
n3 = 5 in lista
if n3 == True:
    n4 = 'faz parte da'
else:
    n4 = 'não foi encontrado na'
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.\n'
      f'Os valores em ordem decrescente são {lista}\n'
      f'O valor 5 {n4} lista!')