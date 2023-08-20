num = int(input('me fale um valor: '))
cont = 0
contnum = 0
while num != 999:
    cont = cont + 1
    contnum = contnum + num
    num = int(input('me fale um número,(se quiser encerrar digite 999): '))
print(f'{cont} números foram contados e a sua soma é {contnum}')
