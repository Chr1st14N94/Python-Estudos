n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
m = (n1 + n2 + n3) / 3

if m < 5:
    print('\033[1;31mReprovado!')
elif 7 > m >=5:
    print('\033[1;33mRecuperação!')
else:
    print('\033[1;34mAPROVADO!')