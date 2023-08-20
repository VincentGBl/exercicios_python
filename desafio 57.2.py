sexo = str(input('qual é o seu sexo? M/F: ')).strip().upper()
while sexo not in 'FfMm':
    sexo = str(input('dados incorretos,qual é o seu sexo? M/F: ')).strip().upper()
print('safe')