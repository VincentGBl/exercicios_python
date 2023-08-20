num = 0
contador = 0
soma = 0
menum = 9999
maiornum = 0
perg = 'ta'
while perg not in 'Ss':
    num = int(input('digite um valor: '))
    soma = soma + num
    contador = contador + 1
    if maiornum < num:
        maiornum = num
    if menum > num:
        menum = num
    perg = str(input('Você quer parar de digitar mais valores? S/N: '))
media = soma / contador
print(f'a média foi {media}, o maior valor é {maiornum} e o menor é {menum}')