n = int(input('me fale um número de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'o número digitado foi: {n}')
print(f'{u} unidades\n{d} dezenas\n{c} centenas\n{m} milhares ')

