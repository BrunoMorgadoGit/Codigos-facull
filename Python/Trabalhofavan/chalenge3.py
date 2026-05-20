import random

num = 5

numeros = []
divisiveis = []

for i in range(20):
    sort = random.randint(1, 50)
    numeros.append(sort)
    if sort % num == 0:
        divisiveis.append(sort)

print(f"Os números sorteados são: {numeros}")
print(f"Os números divisiveis por {num} são: {divisiveis}")