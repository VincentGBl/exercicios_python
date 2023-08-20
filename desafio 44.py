vp = float(input('qual o valor do produto ?: '))
print('digite:\n1)á vista em dinheiro\n2)no cartão á vista\n3)no cartão á prazo em 2 vezes\n4)no cartão á prazo em 3 vezes')
cp = str((input('qual condição vai ser usada?:'))).strip()
if cp == '1':
    vp = vp - (vp * 0.10)
    print(f'o produto ficou no valor de {vp:.2f} REAIS')
elif cp == '2':
    vp = vp - (vp * 0.05)
    print(f'o valor do produto vai ser: {vp:.2f} REAIS')
elif cp == '3':
    print(f'o valor do produtor será {vp:.2f} REAIS')
elif cp == '4':
    vp = vp + (vp * 0.20)
    print(f'o valor do produto será {vp:.2f} REAIS')