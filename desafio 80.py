lista = list()
for v in range(1, 6):
    perg = int(input('digite um valor: '))
    if v == 0 or perg > lista[-1]:
        lista.append(perg)
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                break
            pos = pos + 1