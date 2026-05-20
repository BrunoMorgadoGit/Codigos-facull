Nmin = int(input('Qual é o valor minimo: '))
Nmax = int(input('Qual é o valor maximo: '))

for i in range(Nmin, Nmax + 1):
    if i % 2 == 0:
        print(i, 'Par')
    else:
        print(i, 'Impar')
print('Kbo trutaa')