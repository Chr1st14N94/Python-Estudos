n1 = str(input('Digite seu nome completo: ')).title().split()
print(f'Muito prazer em te conhecer!\n'
      f'Seu primeiro nome é {n1[0]}\n'
      f'Seu último nome é {n1[len(n1)-1]}')