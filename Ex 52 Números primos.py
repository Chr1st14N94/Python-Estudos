num = int(input('Digite um número:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;34m', end='')
        tot += 1
    else:
        print('\033[1;31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(num,tot))
if tot == 2:
    c = '\033[1;34m''É''\033[m'
else:
    c = '\033[1;31m''Não''\033[m'' é'
print('E por isso ele {} primo!'.format(c))