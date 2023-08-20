quasmatriz = list()
matriz = list()
contaleat = 0
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
print(f'[{matriz[0][0]}]-[{matriz[0][1]}]-[{matriz[0][2]}]')
print(f'[{matriz[1][0]}]-[{matriz[1][1]}]-[{matriz[1][2]}]')
print(f'[{matriz[2][0]}]-[{matriz[2][1]}]-[{matriz[2][2]}]')