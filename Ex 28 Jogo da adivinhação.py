from time import sleep
import random
print('\033[1;33m=-'*28)
print('\033[1;34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[1;33m=-\033[m'*28)
n1 = int(input('Em que número eu pensei? '))
n2 = random.randint(0,5)
print('PROCESSANDO....')
sleep(2)
if n1 == n2:
    print(f'\033[1;34mParabéns! O número era {n2} Você venceu! ')
else:
    print(f'\033[1;31mGANHEI! Eu pensei no número {n2} e não no {n1}')