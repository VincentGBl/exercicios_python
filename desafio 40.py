not1 = float(input('primeira nota: '))
not2 = float(input('segunda nota: '))
media = (not1 + not2) // 2
if media < 5.0:
    print('REPROVADO\nBURRÃO KKKKKKKKKKKKKK')
    print('----' * 30)
    print(f'sua média foi {media:.2f}')
elif media >= 7.0:
    print('Que isso em,aprovado cachorro.')
    print('----' * 30)
    print(f'sua média foi {media:.2f}')
elif media >= 5.0 and media <= 6.9:
    print('ta de recuperação,melhor que nada né')
    print('----' * 30)
    print(f'sua média foi {media:.2f}')
