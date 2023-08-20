nums = list()
perg = 0
while True:
    perg = (int(input('digite um valor: ')))
    if perg in nums:
        print('esse valor ja está na lista')
    if perg not in nums:
        nums.append(perg)
        print('Valor colocado com sucesso!')
    pergs = str(input('Adicionar mais um número?\nS/N: ')).upper()
    if pergs == 'N':
        break
print(f'os valores foram {nums}')
print(f'em ordem ficaria {sorted(nums)}')

