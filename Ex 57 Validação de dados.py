n1 = str(input('Informe seu sexo: [M/F] ')).upper()[0]

while n1 not in 'MF':
    n1 = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper()[0]
print(f' Sexo {n1} registrado com sucesso!')