import random

print('Vamos calcular multiplicação?? ')

while True:

    continuar = int(input('1 para Continuar | 0 para Parar '))

    if continuar == 1:
            numero = random.randint(1,15)
            numero1 = random.randint(1,10)
            resultado = numero1 * numero

            print(numero)
            print(numero1)


            Palpite = int(input('Qual é o resultado? '))

            if resultado == Palpite:
                print('Voce acertou!')
            else:
                print('Voce errou')
            
    if continuar == 0:
        break