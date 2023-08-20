peso = float(input('Qual é o seu peso atual?: '))
altura = float(input('e qual é a sua altura(em metros)?: '))
imc = peso // (altura ** 2)
if imc < 18.5:
    print(f'Você está abaixo do peso seu IMC é de {imc}')
elif imc >= 18.5 and imc < 25:
    print(f'Parabéns,você está no seu peso ideal, seu IMC é de {imc}')
elif imc >= 25 and imc < 30:
    print(f'você está sobre-peso,cuidado,seu IMC é de {imc}')
elif imc >= 30 and imc <= 40:
    print(f'você está obeso,seu IMC é de {imc}\n Gordão kkkkkkkkkkkkkkk')
elif imc > 40:
    print(f'pqp ta gordão,teu IMC é de obeso mórbido ,IMC DE: {imc}')