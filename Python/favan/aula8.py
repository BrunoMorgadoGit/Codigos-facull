precolitro = float(input('Qual é o preço do Litro do Combustível? '))
desempenho = float(input('Qual é o desempenho do veículo KM/L? '))
distancia = float(input('Qual é a distância entre as duas cidades em KM? '))

calculo = distancia / desempenho
resultado = calculo * precolitro

print(f'Oque você vai gastar nessa viagem de gasolina é R${resultado:.2f} ')