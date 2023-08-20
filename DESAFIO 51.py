pt = int(input('primeiro termo: '))
rpa = int(input('razão da progressão:'))
termo = pt + (10 - 1) * rpa
for p in range(pt, termo, rpa):
    print(f'{p}', end='-')