sair = False
while not sair:
    n2 = int(input('Pimeiro valor: '))
    n3 = int(input('Segundo valor: '))
    menu = False
    while not menu:
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
            menu = True
        elif n1 > 5:
            print('Opção inválida tente novamente!')
        elif n1 == 5:
            menu = True
            sair = True
        print(f'-==' * 15)
print('Fim do programa.')
