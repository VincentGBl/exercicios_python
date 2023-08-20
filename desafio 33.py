print('diga-me 3 números e eu te direi qual é o maior e o menor entre eles.')
n1 = int(input('primeiro número: '))
n2 = int(input('segundo número: '))
n3 = int(input('terceiro número: '))
maiv = n1
if n2 > n1 and n2 > n3:
    maiv = n2
if n3 > n1 and n3 > n2:
    maiv = n3
#pra saber quem é o menor.
menv = n1
if n2 < n1 and n2 < n3:
    menv = n2
if n3 < n2 and n3 < n1:
    menv = n3
#para saber quem é o menor
print(f'o maior valor é {maiv} e o menor é {menv}')