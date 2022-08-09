n1 = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {n1.count("A")} vezes na frase.\n'
      f'A primeira letra A aparece na {n1.find("A")+1}ª posição.\n'
      f'A última letra A apareceu na {n1.rfind("A")+1}ª posição. ')