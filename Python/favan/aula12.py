option = int(input('1 Para Area do Retangulo | 2 Para Area do Triangulo: '))

if option == 1:
    base = float(input('Qual é a base do retangulo? '))
    altura = float(input('Qual é a altura do retangulo? '))
    area = base * altura
    print(area)

elif option == 2: 
    lado = float(input('Qual é o Lado do Triangulo? '))
    area = lado * lado
    print(area)
