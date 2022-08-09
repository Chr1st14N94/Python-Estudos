import emoji
print('\033[1;31m''{:=^52}''\033[m'.format('MERCADO SANTOS'))
n1=float(input('Valor das compras:'))
print('\033[1;34m''FORMAS DE PAGAMENTO''\033[m')
print('[ 1 ] à vista dinheiro/pic\n[ 2 ] à vista no cartão\n[ 3 ] em até 2x no cartão\n[ 4 ] 3x ou mais no cartão')
n2=int(input('Qual a opção de pagamento:'))
if n2 == 1:
    print('Sua compra de R$:{:.2f} vai custar {:.2f} no final.'.format(n1,n1-n1*10/100))
    print('A opção 1 tem 10% de desconto.')
elif n2 == 2:
    print('Sua compra de R$:{:.2f} vai custar {:.2f} no final.'.format(n1,n1-n1*5/100))
    print('A opção 2 tem 5% de desconto.')
elif n2 == 3:
    print('Sua compra vai custar R$:{:.2f} parcelados em 2x de R$:{} '.format(n1,n1/2))
    print('A opção 3 não tem desconto.')
elif n2 == 4:
    n3=int(input('Quantas parcelas:'))
    n4=float(n1+n1*20/100)
    print('Sua compra de R$:{} fica R$:{} \nparcelado em {}x de R$:{}'.format(n1,n4,n3,n4/n3))
    print('A opção 4 tem um acrécimo de 20%')
else:
    print('\033[1;33m''Opção inválida,tente outra opção!''\033[m')
print(emoji.emojize('\033[1;31m''MERCADO SANTOS ''\033[m''\033[36m''agradece sua preferência!:heart:', use_aliases=True))
