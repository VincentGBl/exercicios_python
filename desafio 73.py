times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Corinthians', 'Internacional', 'Athletico-PR', 'Atlético-MG',
         'Santos', 'América-MG', 'Goiás', 'Bragantino', 'Fortaleza', 'São Paulo', 'Botafogo', 'Ceará', 'Coritiba',
         'Cuiabá', 'Avaí', 'Atlético-GO', 'Chapecoense')
print('=-=-=-' * 40)
print(f'Primeiros colocados){times[0:6]}\nÚltimos colocados){times[-4:]}')
print('=-=-=-' * 40)
print(f'{sorted(times)}')
print('=-=-=-' * 40)
print(f'chapecoense está na posição {times.index("Chapecoense")}')
print('=-=-=-=-=-=-=' * 5, 'Fim do Programa', '=-=-=-=-=-=-=' * 5)
