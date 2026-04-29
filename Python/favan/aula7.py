salario = float(input('Qual é o seu salario? '))
reajuste = float(input('Informe seu reajuste em porcentagem? ').replace("%" , ""))

porcentagem = reajuste/100
total = porcentagem * salario
totalsalario = total + salario


print(f'Seu novo salario será {totalsalario}')