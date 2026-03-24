dias = int(input('Quantos dias: '))
horas = int(input('Quantas horas: '))
minutos = int(input('Quantos minutos: '))
segundos = int(input('Quantos segundos: '))


diaspsegundo = dias * 86400
horassegundo = horas * 3600 
minutosegundos = minutos * 60
resultado = diaspsegundo + horassegundo + minutosegundos + segundos

print(f'O total de segundos é : {resultado}')
