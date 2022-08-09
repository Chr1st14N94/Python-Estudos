from datetime import date
n1 = int(input('Ano de nascimento: '))
hoje = date.today().year
n2 = hoje - n1
print(f'Quem nasceu em {n1} tem {n2} anos em {hoje}')
if n2 > 18:
    print(f'\033[1;31mVocê já deveria ter se alistado há {n2 - 18} anos.\033[m\n'
          f'Seu alistamento foi em {n1 + 18}')
elif n2 < 18:
    print(f'\033[1;34mAinda falta {18 - n2} anos para o alistamento.\033[m\n'
          f'Seu alistamento será em {n1 + 18}')
else:
    print(f'Você tem que se alistar \033[1;33mIMEDIATAMENTE!\033[m neste ano de {hoje}')