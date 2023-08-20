import random
nc = random.randint(0, 5)
nu = int(input('hmmmm,pensei em um número de 0 a 5,qual você acha que foi?: '))
if nu == nc:
    print(f'Parabéns você acertou!! o número foi {nc}, certo?')
else:
    print(f'você errou,o número que pensei foi {nc}')