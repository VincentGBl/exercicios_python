mmdv = 0
somida = 0
hmv = ''
idhmv = 0
for p in range(1, 4 + 1):
    nom = str(input('qual é o seu nome?: '))
    ida = int(input('quantos anos você tem?: '))
    somida = somida + ida
    sex = str(input('e de qual sexo você é?: ')).lower().strip()
    if sex == 'masculino' and ida > idhmv:
        hmv = nom
        idhmv = ida
    if sex == 'feminino' and ida < 20:
        mmdv = mmdv + 1
medidad = somida / 4
print(f'a média da idade dos 4 é {medidad}')
print(f'o homem mais velho se chama {hmv} e tem {idhmv} anos')
print(f'há {mmdv} mulheres menores de 20 anos aqui')




