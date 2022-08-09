s = con = 0

for c in range(1,500,2):
    if c % 3 == 0:
        con = con + 1
        s = s + c
print(f'A soma de todos os {con} valores solicitados é {s}')