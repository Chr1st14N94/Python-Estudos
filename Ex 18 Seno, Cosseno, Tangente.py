import math
an = int(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {an} tem o SENO de {math.sin(math.radians(an)):.2f}\n'
      f'O ângulo de {an} tem o COSSENO de {math.cos(math.radians(an)):.2f}\n'
      f'O ângulo de {an} tem a TANGENTE de {math.tan(math.radians(an)):.2f}')