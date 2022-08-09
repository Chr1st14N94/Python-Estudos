n1 = int(input('Digite um número inteiro: '))
print('-'*38)
n2 = int(input('Escolha uma das bases para conversão:\n'
               '\033[1;32m[ 1 ]\033[m converter para \033[1;32mBINÁRIO\033[m\n'
               '\033[1;33m[ 2 ]\033[m converter para \033[1;33mOCTAL\033[m\n'
               '\033[1;34m[ 3 ]\033[m converter para \033[1;34mHEXADECIMAL\033[m\n'
               '--------------------------------------\n'
               'Sua opção: '))
if n2 == 1:
    print(f'{n1} convertido para BINÁRIO é igual a {bin(n1)[2:]}')
elif n2 == 2:
    print(f'{n1} convertido para OCTAL é igual a {oct(n1)[2:]}')
elif n2 == 3:
    print(f'{n1} convertido para HEXADECIMAL é igual a {hex(n1)[2:]}')
else:
    print(f'Opção errada, você digitou {n2}, tente novamente.')