print('Voce quer saber o volume da lata ou da caixa? ')
lata = bool(input('Você quer calcular a lata? Se sim digite algo, caso ao contrario de ENTER.'))

if lata == True:
    raio = float(input('Qaul é o raio da lata? '))
    altura = float(input('Qual é a altura da lata? '))
    volume = 3.14159 * raio**2 * altura
    print(f'VOLUME DA LATA = {volume:.2f}')

else:
    altura2 = float(input('Qual é a altura da caixa de papelao? '))
    largura = float(input('Qual é a largura da caixa de papelao? '))
    comprimento = float(input('Qual é o comprimento da caixa de papelao? '))
    volume2 = altura2 * largura * comprimento
    print(f'VOLUME DA CAIXA = {volume2:.2f}')
