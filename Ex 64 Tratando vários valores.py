n1 = s = c = 0
while n1 != 999:
    n1 = int(input('Digite um número [999 para parar]: '))
    if n1 != 999:
        s = s + n1
        c = c + 1
print(f'Você digitou {c} números e a soma entres eles foi {s}')