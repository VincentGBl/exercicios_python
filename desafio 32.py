ano = int(input('me fale um ano e direi se ele é bissexto ou não: '))
vano = ano % 4
if vano == 0:
    print('este é sim um ano bissexto!')
else:
    print("este ano não é bissexto!")