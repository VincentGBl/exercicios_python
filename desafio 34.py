salario = float(input('qual é o seu salário?: '))
if salario > 1250.00:
    aumento = (salario * 0.10) + salario
    print(f'Parabéns,você ganhou um aumento,seu novo salário será de R${aumento:.2f}')
else:
    aumento = (salario * 0.15) + salario
    print(f'Parabéns,você ganhou um aumento,seu novo salário será de R${aumento:.2f}')