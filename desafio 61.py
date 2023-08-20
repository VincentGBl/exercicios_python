pt = int(input('primeiro termo: '))
termos = pt
ra = int(input('razão: '))
cont = 1
while cont <= 10:
    print(f'{termos}', end='=>')
    cont = cont + 1
    termos = termos + ra
print('fim.')