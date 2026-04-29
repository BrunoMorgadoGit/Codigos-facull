while True:
    num = int(input('Digite um numero para tabuada: '))
    if num == 0:
        print(' 0 = encerrar')
        break

    Nmin = int(input('Qual é o valor minimo da tabuada: '))
    Nmax = int(input('Qual é o valor maximo da tabuada: '))
    print('Tabuada do', num, 'minimo: ', Nmin, 'maximo: ', Nmax)
    i = Nmin
    while i <= Nmax:
        res = num * i
        print(num, "x", i, "=", res)
        i +=1
    print('Fim do programa')
