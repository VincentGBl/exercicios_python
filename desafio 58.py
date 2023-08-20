import random
cdp = 0
nc = random.randint(0, 10)
nu = int(input('hmmmm,pensei em um número de 0 a 10,qual você acha que foi?: '))
while nu != nc:
    nu = int(input('Você errou,tente novamente!!: '))
    cdp = cdp + 1
print(f'parabéns,você me ganhou,eu pensei no número {nc} e você também! {nu}\nvocê ganhou em {cdp} tentativas')