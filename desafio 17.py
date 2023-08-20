import math
cco = float(input('quanto mede o cateto oposto?(em centímetros):'))
cca = float(input('quanto mede o cateto adjascente?(em centímetros): '))
ec = cco ** 2 + cca ** 2
ehip = math.sqrt(ec)
print(f'o comprimento da hipotenusa será igual a {ehip:.2f} centímetros.')
