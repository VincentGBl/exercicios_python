contanim = 0
contani = 0
for a in range(1, 7 + 1):
    ani = int(input('em qual ano você nasceu?: '))
    if 2022 - ani < 18:
        contani = contani + 1
    if 2022 - ani >= 18:
        contanim = contanim + 1
print(f'existem {contani} pessoas que nao são maiores de idade e {contanim} pessoas que ja são maiores de idade')