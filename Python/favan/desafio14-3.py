comeco = int(input('Qual é o numero inicial da lista: '))
fim = int(input('Qual é o numero final da lista: '))
dividido = int(input('Com qual valor voce quer que divida: '))

if comeco <= fim:
    for i in range(comeco, fim +1):
       if i%dividido == 0:
            print(i, 'divisivel por',dividido)
else:
    print('lista invalida')
