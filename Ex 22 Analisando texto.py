n1 = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
n2 = n1.count(' ')
n3 = n1.split()

print(f'Seu nome em maiúsculo é {n1.upper()}\n'
      f'Seu nome em minúsculo é {n1.lower()}\n'
      f'Seu nome ao todo tem {len(n1)-n2} letras\n'
      f'Seu primeiro nome é {n3[0]} e ele tem {len(n3[0])} letras.')