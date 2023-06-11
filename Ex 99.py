from random import randint


def maior(*num):
    mai = 0
    print('-=' * 24)
    print('Analisando valores passados.....')
    for c in num:
        print(f'{c}', end=' ')
        if c > mai:
            mai = c
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10), randint(1, 10),)
maior(randint(1, 10), randint(1, 10),)
maior(randint(1, 10))
maior()
