lista = []
lista2 = []
lista3 = []
while True:
    valor = (int(input('digite um valor: ')))
    lista.append(valor)
    if valor % 2 == 0:
        lista2.append(valor)
    elif valor % 2 != 0:
        lista3.append(valor)
    pergs = str(input('Adicionar mais números?(S/N): ')).strip().upper()
    if pergs not in 'SN':
        pergs = pergs[0]
    if pergs in 'N':
        break
print(f'a lista sem critérios ficou: {lista}')
print(f'a lista de pares ficou: {lista2}')
print(f'a lista de impares ficou: {lista3}')
