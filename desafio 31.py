vkm = int(input('quantos kilomêtros a sua viagem ira ter?: '))
if vkm <= 200:
    preco = vkm * 0.50
    print(f'a sua passagem irá custar R${preco:.2f} REAIS.')
else:
    preco = vkm * 0.45
    print(f'a sua passagem irá custar R${preco:.2f} REAIS.')