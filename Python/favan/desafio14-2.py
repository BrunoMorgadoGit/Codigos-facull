a = 0
b = 0
for numerospar in range(1, 101):
    if numerospar%2 == 0:
        a = a + numerospar
        print(f'A soma dos Pares: {a}')
        

for numeroimpar in range(1,101):
    if numeroimpar%2 == 1:
        b = b + numeroimpar
        print(f'A soma dos Impares: {b}')

print(f'A soma dos dois juntos é: {a + b}')