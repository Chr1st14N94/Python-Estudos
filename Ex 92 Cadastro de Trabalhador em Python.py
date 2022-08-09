from datetime import datetime
cont = 0
inf = {}
while cont == 0:
    inf['nome'] = str(input('Nome: ')).title()
    n1 = int(input('Ano de Nascimento: '))
    inf['idade'] = datetime.now().year - n1
    inf['ctrl'] = int(input('Carteira de Trabalho: '))
    if inf['ctrl'] == 0:
        break
    inf['contratação'] = int(input('Ano de Contratação: '))
    inf['salário'] = float(input('Salário: R$: '))
    inf['aponsentadoria'] = inf['contratação'] - n1 + 30
    cont += 1
print('==--' * 9)
for c, i in inf.items():
    print(f'- {c} tem o valor - {i}')
