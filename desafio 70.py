perg = 'safe'
npmb = 'ta'
pmb = 9999
totdg = 0
contp = 0
while True:
    ndp = str(input('qual é o nome do produto?: '))
    pdp = float(input('qual o preço do produto citado?: '))
    totdg = totdg + pdp
    if pdp > 1000:
        contp = contp + 1
    if pdp < pmb:
        pmb = pdp
        npmb = ndp
    perg = str(input('mais algum produto a ser adicionado?: ')).strip().upper()
    if perg == 'N':
        break
print(f'o total da sua compra foi: {totdg}\ncom {contp} produtos sendo mais de 1000 reais\no produto mais barato foi {npmb}')

