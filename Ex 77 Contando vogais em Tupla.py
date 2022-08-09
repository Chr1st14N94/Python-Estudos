n1 = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR',
      'MERCADO','PROGRAMADOR','FUTURO',)
for c in n1:
    print(f'\nNa palavra {c} temos ',end='')
    for i in c:
        if i in 'AEIOU':
            print(f'{i} ',end='')

