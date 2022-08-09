n1 = int(input('Quer ver a Tabuada de qual valor? '))
while True:
    print('=-' * 15)
    for c in range(1,11):
        print(f'{n1} X {c} = {n1*c}')
    print('=-'*15)
    n1 = int(input(f'Quer ver outro valor? '))
    if n1 == 0:
        break
