soma = 0
conta = 0
while True:
    num = int(input('digile um valor (999 para parar): '))
    if num == 999:
        break
    soma = soma + num
    conta = conta + 1
print(f'a soma foi {soma} e foram contados {conta} números')
