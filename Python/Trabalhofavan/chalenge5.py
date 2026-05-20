import random

escolha = int(input('Escolha uma opção: ordem normal(1) ou ordem inversa(2): '))

vetor = []

for i in range(10):
    vetor.append(random.randint(1, 50))
print(vetor)

if escolha == 1:
    print('Vetor na ordem normal:')
    for i in range(0, len(vetor)):
        print(vetor[i], end=', ')

else:
    print('Vetor na ordem inversa:')
    for i in range(len(vetor) - 1, -1, -1):
        print(vetor[i], end=', ')