dados = []
pessoas = dict()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).title()
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('Erro! Por favor digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    dados.append(pessoas.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break
    elif resp != 'S':
        print('Erro, digite S ou N.')
print('=-' * 10)
print(dados)
print('=-' * 10)
print(f'A) ao todo temos {len(dados)} pessoas cadastradas.')
media = soma / len(dados)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end=' ')
for p in dados:
    if p["sexo"] == 'F':
        print(f'{p["nome"]}', end='')
print()
print(f'D) Lista das pessoas que estão acima da média ')
for p in dados:
    if p["idade"] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()