idade = int(input('eai atleta,quantos anos você tem? : '))
if idade <= 9:
    print('CLASSIFICAÇÃO:\nAtleta Mirim')
elif idade > 9 and idade <= 14:
    print('CLASSIFICAÇÃO\nAtleta Infantil')
elif idade > 14 and idade <= 19:
    print('CLASSIFICAÇÃO\nAtleta Junior')
elif idade == 20:
    print('CLASSIFICAÇÃO\nAtleta Sênior')
elif idade > 20:
    print('CLASSIFICAÇÃO\nAtleta Master')