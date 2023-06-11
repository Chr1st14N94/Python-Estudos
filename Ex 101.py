def voto(a):
    from datetime import datetime
    idade = datetime.now().year - a
    if idade < 16:
        return f'Com {idade} anos NÃO VOTA! '
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos o VOTO É OPCIONAL!'
    else:
        return f'Com {idade} anos VOTO É OBRIGATÓRIO!'


print('¬' * 30)
print(voto(int(input('Em que ano você nasceu? '))))