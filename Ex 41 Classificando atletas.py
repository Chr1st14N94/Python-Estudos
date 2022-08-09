from datetime import date
n1 = int(input('Ano de nascimento: '))
hoje = date.today().year
idade = hoje - n1
if idade <= 9:
    clas = 'MIRIM'
elif idade <= 14:
    clas = 'INFANTIL'
elif idade <= 19:
    clas = 'JÚNIOR'
elif idade <= 25:
    clas = 'ADULTO'
else:
    clas = 'MASTER'
print(f'O atleta tem {idade} anos.\n'
      f'Classificação: {clas}')