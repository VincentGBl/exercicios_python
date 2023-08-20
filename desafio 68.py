from random import randint
condvi = 0
while True:
    j = int(input('me fale um numero e vamos jogar par ou ímpar!!: '))
    ipj = str(input('você que jogar como Impar ou como Par?: ')).strip().upper()
    p = randint(0, 10)
    if ipj == 'PAR' and (j + p) % 2 == 0:
        print(f'Droga,você me ganhou!,eu escolhi o numero {p} e você o {j}')
    if ipj == 'IMPAR' and (j + p) % 2 == 0:
        print(f'haha eu te ganhei,eu escolhi o numero {p} e você o {j},você me ganhou um total de {condvi} vezes')
        break
    if ipj == 'IMPAR' and (j + p) % 2 != 0:
        print(f'Uou,você me ganhou!,eu escolhi o numero {p} e você o {j}')
    if ipj == 'PAR' and (j + p) % 2 != 0:
        print(f'hahaha eu te ganhei,eu escolhi o numero {p} e você o {j},você me venceu um total de {condvi} vezes')
        break
    condvi = condvi + 1
print('acabou foda-se')
