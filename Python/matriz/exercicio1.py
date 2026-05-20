import random

matriz = [[random.randint(0, 10) for _ in range(3)] for _ in range(3)]

for linha in matriz:
    print(linha)

soma_principal = sum(matriz[i][i] for i in range(3))

n = len(matriz)
soma_secundaria = sum(matriz[i][n - 1 - i] for i in range(n))

print(f"\nSoma da diagonal principal:  {soma_principal}")
print(f"Soma da diagonal secundária: {soma_secundaria}")

