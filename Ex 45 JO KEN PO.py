from time import sleep
import random
print('-'*45)
n1 = int(input('Suas opções:\n'
             '\033[1;34m[ 0 ] PEDRA\033[m\n'
               '\033[1;32m[ 1 ] PAPEL\033[m\n'
               '\033[1;31m[ 2 ] TESOURA\033[m\n'
               'Qual é sua jogada? '))

n2 = random.randint(0,2)

if n1 == 0 or n1 == 1 or n1 == 2:
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    if n1 == 0 and n2 == 2:
        jog = 'PEDRA'
        pc = 'TESOURA'
        res = '\033[1;34mVocê VENCEU!\033[m'
    elif n1 == 1 and n2 == 0:
        jog = 'PAPEL'
        pc = 'PEDRA'
        res = '\033[1;34mVocê VENCEU!\033[m'
    elif n1 == 2 and n2 == 1:
        jog = 'TESOURA'
        pc = 'PAPEL'
        res = '\033[1;34mVocê VENCEU!\033[m'
    elif n2 == 0 and n1 == 2:
        jog = 'TESOURA'
        pc = 'PEDRA'
        res = '\033[1;31mVocê Perdeu!\033[m'
    elif n2 == 1 and n1 == 0:
        jog = 'PEDRA'
        pc = 'PAPEL'
        res = '\033[1;31mVocê Perdeu!\033[m'
    elif n2 == 2 and n1 == 1:
        jog = 'PAPEL'
        pc = 'TESOURA'
        res = '\033[1;31mVocê Perdeu!\033[m'
    elif n1 == 0 and n2 == 0:
        jog = 'PEDRA'
        pc = 'PEDRA'
        res = '\033[1;33mEMPATOU!\033[m'
    elif n1 == 1 and n2 == 1:
        jog = 'PAPEL'
        pc = 'PAPEL'
        res = '\033[1;33mEMPATOU!\033[m'
    elif n1 == 2 and n2 == 2:
        jog = 'TESOURA'
        pc = 'TESOURA'
        res = '\033[1;33mEMPATOU!\033[m'
    print('-='*12)
    print(f'Jogador jogou {jog}\n'
          f'Computador jogou {pc}\n'
          f'{res}')
    print('-='*12)
else:
    print('-'*32)
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
    print('-'*32)

