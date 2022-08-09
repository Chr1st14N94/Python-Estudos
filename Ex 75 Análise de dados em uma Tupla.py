n1 = (int(input('Digite um número: ')),int(input('Digite outro número: ')),int(input('Digite mais um número: ')),
      int(input('Digite o último número: ')))
print(f'Você digitou os valores {n1}')
print(f'O número 9 apareceu {n1.count(9)} vez(es).')
if 3 in n1:
    print(f'O valor 3 apareceu na {n1.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nunhuma posição.')
print(f'Os valores pares digitados foram ', end='')
for c in n1:
    if c % 2 == 0:
        print(c, end=" ")