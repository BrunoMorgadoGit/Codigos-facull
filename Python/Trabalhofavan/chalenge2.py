import random

numeros = []
soma = 0
quant_pares = 0

for i in range(20):
    numero = random.randint(1, 50)
    numeros.append(numero)

    if numero % 2 == 0:
        soma += numero
        quant_pares += 1

print(numeros)

if quant_pares > 0:
    media = soma / quant_pares
    print(f"A média dos números pares é {media:.2f}")
else:
    print("Não foram sorteados números pares.")