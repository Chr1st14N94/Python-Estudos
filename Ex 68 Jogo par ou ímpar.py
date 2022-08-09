from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
cont = 0
while True:
    print('=-' * 15)
    n1 = int(input('Diga um valor: '))
    n2 = str(input(f'Par ou Ímpar? [P/I]: ')).upper()[0]
    print('=-' * 15)
    pc = randint(1,11)
    cont = cont + 1
    soma = n1 + pc
    total = soma % 2
    if total == 1:
        if n2 == 'I':
           r1 = 'ÍMPAR'
           r2 = 'VENCEU'
        else:
            r1 = 'ÍMPAR'
            r2 = 'PERDEU'
    else:
        if n2 == 'P':
            r1 = 'PAR'
            r2 = 'VENCEU'
        else:
            r1 = 'PAR'
            r2 = 'PERDEU'


    print(f'Você jogou {n1} e o computador jogou {pc}. Total de {soma} DEU {r1}\n'
          f'Você {r2}\n'
          f'Vamos jogar novamente...')