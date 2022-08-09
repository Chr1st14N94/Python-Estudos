totmaior = man = mulher = 0
while True:
    print('Cadastre uma pessoa')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        totmaior = totmaior + 1
    if sexo == 'M':
        man = man + 1
    if sexo == 'F' and idade < 20:
        mulher = mulher + 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totmaior}\n'
              f'Ao todo temos {man} homem cadastrado(s)\n'
              f'E temos {mulher} mulher(es) com menos de 20 anos.')

