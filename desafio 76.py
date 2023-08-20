prec = ('Frango', 14, 'Leite', 8.90, 'creme de leite', 4.50, 'macarrão', 6)
print('-' * 40)
print(f'{"TABELA DE PREÇOS":^40}')
print('-' * 40)
for p in range(0, len(prec)):
    if p % 2 == 0:
        print(f'{prec[p]:.<20}', end='')
    if p % 2 != 0:
        print(f'{prec[p]:.>20.2f}')
print('-' * 40)