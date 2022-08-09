n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

if n1 > n2:
    print(f'O primeiro número é maior, valor {n1}')
elif n2 > n1:
    print(f'O segundo número é maior, valor {n2}')
else:
    print(f'Os dois números são IGUAIS. valor {n1}')