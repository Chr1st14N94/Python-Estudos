from random import randint
num = (randint(0,10),randint(0,10),randint(0,10),randint(0,10))
for c in num:
    print(c, end=' ')
n1 = sorted(num)
print(f'\nO menor número é {n1[0]}\n'
      f'O maior número é {n1[-1]}')