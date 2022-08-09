n1 = float(input('Valor da casa: '))
n2 = float(input('Salário do comprador: R$ '))
n3 = int(input('Quantos anos de financiamento? '))
parc = n3 * 12
pres = n1 / parc
sal = (pres * 100) / n2
if sal > 30:
    resul = '\033[1;31mNEGADO!'
else:
    resul = 'pode ser \033[1;34mCONCEDIDO!'
print(f'Para pagar uma casa de R$:{n1:.2f} em {n3} ano com {parc} parcelas,\na prestação será de R$:{pres:.2f}, '
      f'{sal:.1f}% do seu salário, Empréstimo {resul}')