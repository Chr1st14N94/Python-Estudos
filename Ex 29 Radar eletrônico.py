n1 = int(input('Qual é a velocidade atual do carro? '))

if n1 > 80:
    print(f'\033[1;31mMultado! Você excedeu o limite permitido que é de 80Km/h\n'
          f'Você deve pagar a multa de \033[33mR$:{(n1 - 80)*7:.2f}')
print('\033[1;36mTenha um bom dia! Dirija com segurança!')