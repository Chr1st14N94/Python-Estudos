sair = False
n2 = int(input('Pimeiro valor: '))
n3 = int(input('Segundo valor: '))
while not sair:
    n1 = int(input('[  1  ] Somar\n'
                   '[  2  ] Multiplicar\n'
                   '[  3  ] Maior\n'
                   '[  4  ] Novos Números\n'
                   '[  5  ] Sair do Programa\n'
                   '>>>>> Qual é sua opção? '))
    if n1 == 1:
        print(f'A soma entre {n2} e {n3} é {n2 + n3}')
    elif n1 == 2:
        print(f'O resultado de {n2} X {n3} é {n2 * n3}')
    elif n1 == 3:
        if n2 > n3:
            print(f'Entre {n2} e {n3} o maior valor é o {n2}')
        elif n2 < n3:
            print(f'Entre {n2} e {n3} o maior valor é o {n3}')
        else:
            print(f'Os doi números tem o mesmo valor!')
    elif n1 == 4:
        print('Informe os novos valores.')
        n2 = int(input('Pimeiro valor: '))
        n3 = int(input('Segundo valor: '))
    elif n1 > 5:
        print('Opção inválida tente novamente!')
    elif n1 == 5:
        sair = True
    print(f'-==' * 15)

print('Fim do programa.')