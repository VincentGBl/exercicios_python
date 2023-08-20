pt = int(input('primeiro termo: '))
termos = pt
ra = int(input('razão: '))
perg = 10
cont = 1
total = 0
while perg != 0:
    total = total + perg
    while cont <= total:
        print(f'{termos}', end='=>')
        cont = cont + 1
        termos = termos + ra
    perg = int(input('quantos termos vc ainda quer ver?(0 para parar): '))
print('fim.')

