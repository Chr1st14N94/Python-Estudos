lista = list()
med = list()
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    med.append(lista[:])
    lista.clear()
    n2 = str(input('Quer continuar? [S/N] ')).upper()[0]
    if n2 == 'N':
        break
print('Nº    NOME     MÉDIA')
for c,i in enumerate(med):
    print(f'{c}    {i[0].title()}     {(i[1]+i[2])/2:.2f}')
while True:
    resp = int(input('Mostar notas de qual aluno? (999 interrompe): '))
    if resp != 999:
        print(f'Notas de {med[resp][0].title()} são {med[resp][1:]}')
    else:
        break