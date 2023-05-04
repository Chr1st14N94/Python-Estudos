pessoa = dict()
gente = list()

while True:
    gente.append(str(input('Nome: ')).upper())
    sexo = str(input('Sexo: [M/F] ')).upper()[0]
    while sexo not in "MF":
        print('ERRO! Resposta apenas [M/F]. ')
        sexo = str(input('Sexo: [M/F] ')).upper()[0]
    gente.append(sexo)
    gente.append(int(input('Idade: ')))
    cont = str(input('Quer continuar? [S/N]: ')).upper()[0]
    for c in gente:
        pessoa
    if cont == 'N':
        break

print(f'{gente}')