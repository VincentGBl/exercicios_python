pares = list()
impares = list()
numeros = list()
for n in range(0, 7):
    valores = (int(input('digite um valor: ')))
    if valores % 2 == 0:
        pares.append(valores)
    else:
        impares.append(valores)
numeros.append(pares)
numeros.append(impares)
#print(numeros)
print(f'os números pares digitados foram os : {sorted(numeros[0][0:])}')
print(f'os números ímpares digitados foram os : {sorted(numeros[1][0:])}')
