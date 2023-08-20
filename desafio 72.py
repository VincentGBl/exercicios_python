numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
nums = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
while True:
    num = int(input('digite um número: '))
    if num == 0:
        print(f'{numero[0]}')
    if num == 1:
        print(f'{numero[1]}')
    if num == 2:
        print(f'{numero[2]}')
    if num == 3:
        print(f'{numero[3]}')
    if num == 4:
        print(f'{numero[4]}')
    if num == 5:
        print(f'{numero[5]}')
    if num == 6:
        print(f'{numero[6]}')
    if num == 7:
        print(f'{numero[7]}')
    if num == 8:
        print(f'{numero[8]}')
    if num == 9:
        print(f'{numero[9]}')
    if num == 10:
        print(f'{numero[10]}')
    if num == 11:
        print(f'{numero[11]}')
    if num == 12:
        print(f'{numero[12]}')
    if num == 13:
        print(f'{numero[13]}')
    if num == 14:
        print(f'{numero[14]}')
    if num == 15:
        print(f'{numero[15]}')
    if num == 16:
        print(f'{numero[16]}')
    if num == 17:
        print(f'{numero[17]}')
    if num == 18:
        print(f'{numero[18]}')
    if num == 19:
        print(f'{numero[19]}')
    if num == 20:
        print(f'{numero[20]}')
    if num not in (nums[0:]):
        print('o número digitado está fora do parâmetro de 0 a 20,tentar novamente por favor.')
    perg = str(input('terminar a pesquisa? S/N\n:')).upper()
    if perg not in 'N':
        break

