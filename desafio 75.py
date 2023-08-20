contp = 0
num = (int(input('primeiro valor: ')), int(input('segundo valor: ')), int(input('terceiro valor: ')),
       int(input('quarto valor: ')))
for p in num:
    if p % 2 == 0:
        contp += 1
print(f'{num.count(9)}')
print(f'{num.index(3) + 1}')
print(f'{contp}')