lista = []
cont5 = 0
while True:
    perg = int(input('digite um valor: '))
    lista.append(perg)
    if perg == 5:
        cont5 += 1
    pergs = str(input('Adicionar mais números?\nS/N: ')).upper().strip()
    if pergs not in 'SN':
        pergs = pergs[0]
    if pergs in 'N':
        break
print(f'foram adicionados {len(lista)} números')
print(f'em ordem decrescente: {sorted(lista, reverse=True)}')
if cont5 != 0:
    print('Sim,a lista contém o número 5')
else:
    print('Não,a lista não contém o número 5')