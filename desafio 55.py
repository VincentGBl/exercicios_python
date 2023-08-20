menpes = 999999
maipes = 0
for p in range(1,5 + 1):
    peso = float(input('qual é o seu peso?: '))
    if peso > maipes:
        maipes = peso
    if peso < menpes:
        menpes = peso
print(f'o maior peso foi {maipes} e o menor peso foi {menpes}')
