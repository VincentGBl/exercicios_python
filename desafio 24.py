cidade = str(input('diga o nome de uma cidade: '))
cm = cidade.upper()
cs = cm.split()
cie = cs[0]
resposta = 'SANTO' in cie
print(f'{resposta}')


