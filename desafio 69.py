idad = 0
sex = 's'
perg = 'y'
contdgent = 0
cpmi = 0
ch = 0
cmmv = 0
while True:
    idad = int(input('quantos anos você tem?: '))
    sex = str(input('qual é o seu sexo? M/F: ')).upper()
    perg = str(input('você quer continuar? S/N: ')).upper()
    contdgent = contdgent + 1
    if idad >= 18:
        cpmi = cpmi + 1
    if sex == 'M':
        ch = ch + 1
    if idad < 20 and sex == 'F':
        cmmv = cmmv + 1
    if perg == 'N':
        break
print(f'foram analisadas {contdgent} pessoas\n{ch} eram homens\n{cpmi} eram maiores de idade\n{cmmv} eram mulheres menores de 20')