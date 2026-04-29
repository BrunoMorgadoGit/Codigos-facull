capacidade = float(input('Qual é a capacidade maxima do elevador em kg? '))
peso = float(input('Qual é o peso das 5 pessoas juntas? '))

if peso > capacidade:
    print('Cara, vai dar ruim')
else: 
    print('Pode subir!')
