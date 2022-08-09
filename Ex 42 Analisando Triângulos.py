print('\033[31m''--=' *30)
print('\033[1;34;42m''Analisador de Triangulos:''\033[m')
print('\033[31m''--=''\033[m' *30)
r1=float(input('Primeiro Segmento:'))
r2=float(input('Segundo Segmento'))
r3=float(input('Terceiro Segmento'))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('\033[36m''Os segmentos acima podem formar um triangulo:',end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('\033[31m''Os segmentos acima não podem formar um triangulo!')