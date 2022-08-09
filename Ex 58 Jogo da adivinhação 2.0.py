from random import randint
pc = randint(1,11)
cont = 0
n1 = 0
while n1 != pc:
    n1 = int(input('Qual é seu palpite? '))
    if n1 > pc:
        print('MENOS... Tente mais uma vez.')
    elif n1 < pc:
        print('MAIS... Tente mais uma vez.')
    cont = cont + 1
print(f'Acertou com {cont} tentativas. Parabéns.')

