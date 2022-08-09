aluno = dict()
aluno['Nome'] = str(input('Nome: ')).title()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
for c,i in aluno.items():
    print(f'- {c} é igual a {i}')
    if aluno['Média'] >= 7:
        resp = 'APROVADO'
    elif aluno['Média'] < 5:
        resp = 'REPROVADO'
    else:
        resp = 'RECUPERAÇÃO'
print(f'- situação é igual a {resp}')

