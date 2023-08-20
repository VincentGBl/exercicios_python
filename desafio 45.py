import random
valores = random.randint(0, 2)
jkplis = ['pedra', 'papel', 'tesoura']
ju = str(input('vamos jogar pedra,papel e tesoura?\nescreva a sua jogada!: ')).lower()
jc = jkplis[valores]
if ju == 'pedra' and jc == 'tesoura':
    print(f'Droga,você me ganhou,eu coloquei {jc} e você {ju}')
elif ju == 'tesoura' and jc == 'papel':
    print(f'Droga,você me ganhou,eu coloquei {jc} e você {ju}')
elif ju == 'papel' and jc == 'pedra':
    print(f'Droga,você me ganhou,eu coloquei {jc} e você {ju}')
elif jc == 'pedra' and ju == 'tesoura':
    print(f'Haha,eu te ganhei,eu coloquei {jc} e você {ju}')
elif jc == 'tesoura' and ju == 'papel':
    print(f'Haha,eu ganhei!,eu coloquei {jc} e você {ju}')
elif jc == 'papel' and ju == 'pedra':
    print(f'Haha,eu ganhei!,eu coloquei {jc} e você {ju}')
else:
    print(f'hahaha parece que nós empatamos,{jc} com {ju}')
