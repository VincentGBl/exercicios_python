quasmatriz = list()
matriz = list()
contaleat = 0
somador = 0
somadorl = 0
somadorc = 0
for m in range(0, 3):
    quasmatriz.append(int(input(f'digite o valor da posição [0,{contaleat}]: ')))
    contaleat += 1
matriz.append(quasmatriz[:])
quasmatriz.clear()
contaleat = 0
for n in range(0, 3):
    quasmatriz.append(int(input(f'digite o valor da posição [1,{contaleat}]: ')))
    contaleat += 1
matriz.append(quasmatriz[:])
quasmatriz.clear()
contaleat = 0
for o in range(0, 3):
    quasmatriz.append(int(input(f'digite o valor da posição [2,{contaleat}]: ')))
    contaleat += 1
matriz.append(quasmatriz[:])
quasmatriz.clear()
for l in range(0, 3):
    for c in range(0, 3):
        somador += matriz[l][c]
for l in range(0, 3):
    for c in range(2, 3):
        somadorc += matriz[l][c]
for l in range(1, 2):
    for c in range(0, 3):
        somadorl += matriz[l][c]
print(f'[{matriz[0][0]}]-[{matriz[0][1]}]-[{matriz[0][2]}]')
print(f'[{matriz[1][0]}]-[{matriz[1][1]}]-[{matriz[1][2]}]')
print(f'[{matriz[2][0]}]-[{matriz[2][1]}]-[{matriz[2][2]}]')
print(f'\na soma será {somador}')
print(f'a soma da coluna 3 será {somadorc}')
print(f'a soma da linha 2 será {somadorl}')