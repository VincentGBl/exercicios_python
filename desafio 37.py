numc = 0
num = int(input('me fale um número (inteiro): '))
opção = (input('agora me diga se você quer tornar esse número em:\n1)binário\n2)hexadecimal\n3)octal\n(escreva a opção que você quiser): ')).strip()
if opção == '1':
    numc = bin(num)
    print(f'{numc}')
elif opção == '2':
    numc = hex(num)
    print(f'{numc}')
elif opção == '3':
    numc = oct(num)
    print(f'{numc}')
else:
    print('você não escolheu de 1 a 3!')