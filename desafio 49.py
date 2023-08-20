result = 0
multiplicador = 0
numero = int(input('o número de qual tabuada vc vai querer?: '))
print('tabuada:')
for t in range(0, 10):
    multiplicador = multiplicador + 1
    result = multiplicador * numero
    print(result)

