from time import sleep
from random import randint
palpites = list()
mascpalpites = list()
perg = int(input('quantos jogos vão ser feitos?: '))
print(f'seus palpites computados foram:')
for j in range(perg):
    for n in range(0, 6):
        mascpalpites.append(randint(0, 60))
    palpites.append(mascpalpites[:])
    mascpalpites.clear()
    print(sorted(palpites[j]))
    sleep(2)