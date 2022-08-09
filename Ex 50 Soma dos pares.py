s = 0
for c in range(1,7):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        s = s + n1
print(f'A soma dos valores pares é {s}')