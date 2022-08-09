n2 = ('Zero','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ','ONZE',
      'DOZE','TREZE','QUATORZE','QUINZE','DEZESSEIS','DEZESETE','DEZOITO','DEZENOVE','VINTE')
while True:
    n1 = int(input('Digite um número entre 0 a 20: '))
    if n1 > 20:
        n1 = int(input('Tente novamente. Digite um número entre 0 a 20: '))
    if n1 < 0:
        n1 = int(input('Tente novamente. Digite um número entre 0 a 20: '))
    print(f'Você digitou o número {n2[n1]}')
    n3 = ' '
    while n3 not in 'SN':
        n3 = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if n3 in 'N':
        break
