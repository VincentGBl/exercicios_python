lista = list()
for v in range(1, 6):
    lista.append(int(input('digite um valor: ')))
#print(lista)
print(f'Você digitou {lista}')
print(f'Maior: {max(lista)}\nMenor: {min(lista)}')