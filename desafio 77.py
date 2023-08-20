pal = ('carro', 'moto', 'geladeira', 'manutenção')
for p in pal:
    print(f'\nna palavra {p.upper()}, temos as vogais: ', end=' ')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')