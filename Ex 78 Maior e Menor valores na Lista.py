n1 = list()
maior = menor = cont = 0
for c in range(0, 5):
    n1.append(int(input(f'Digite um valor para a posição {c+1}: ')))
    cont = cont + 1
    if c == 0:
        maior = menor = n1[0]
    else:
        if n1[c] > maior:
            maior = n1[c]
        if n1[c] < menor:
            menor = n1[c]
print(f'O maior número foi {maior}, na posição ', end='')
for i, v in enumerate(n1):
    if v == maior:
        print(f'{i+1}...', end='')
print()
print(f'O menor número foi {menor}, na posição ', end='')
for i, v in enumerate(n1):
    if v == menor:
        print(f'{i+1}...', end='')
