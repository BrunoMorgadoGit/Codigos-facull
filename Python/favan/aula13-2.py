total = 0

while True:
    gasto = float(input("Digite o valor gasto (0 para finalizar): R$ "))

    if gasto == 0:
        break

    total += gasto

print(f"Total gasto no dia: R$ {total:.2f}")

 