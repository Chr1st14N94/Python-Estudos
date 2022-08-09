cont = soma = 0
while True:
    n1 = int(input('Digite um valor (999 para parar): '))
    if n1 == 999:
        break
    cont = cont + 1
    soma = soma + n1

print(f'A soma dos {cont} valores foi {soma}')