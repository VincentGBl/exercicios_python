vel = int(input('a quantos kilometros o carro estava por hora?: '))
if vel <= 80:
    print('tudo dentro dos conformes.\n---FIM---')
else:
    custo = (vel - 80) * 7
    print(f'você foi multado,e custo de será de R${custo},00 REAIS.')