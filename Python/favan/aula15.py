numeroint = int(input('Digite o limite da sequência Fibonassi: '))
# one = 1 + 1
# two = 1 + 2 
# three = 2 + 3
# four = 3 + 5
# five = 5 + 8
# six = 8 + 13
# seven = 13 + 21
# eight = 21 + 34
# nine = 34 + 55
# ten = 55 + 89 = 144
n1 = 1 
n2 = 1
if  numeroint <= 2:
    print(n1,n2)
else: 
    for i in range(3,numeroint + 1, 1):
        resultado = n1 + n2
        print(resultado)
        n1 = n2
        n2 = resultado     