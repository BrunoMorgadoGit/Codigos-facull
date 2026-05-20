import random

a = []
pares = 0
impares = 0

for i in range(10):
    a.append(random.randint(1, 50))

    if a[i] % 2 == 0:
        pares += 1
    else:
        impares += 1

print(a)
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")