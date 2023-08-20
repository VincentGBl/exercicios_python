tabu = (int(input('valor da tabuada: ')))
while True:
    for t in range(0,11):
        print(f'{tabu} X {t} ->',end='')
        print(tabu * t)
    tabu = (int(input('qual tabuada você quer agora(se quiser parar digite um número negativo: ')))
    if tabu < 0:
        break
print('fim')
