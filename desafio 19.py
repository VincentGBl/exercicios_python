import random
pa = str(input('nome do primeiro aluno: '))
sa = str(input('nome do segundo aluno: '))
ta = str(input('nome do terceiro aluno: '))
qa = str(input('nome do quarto aluno: '))
print(f'quem irá apagar o quadro será : \n {random.choice([pa, sa, ta, qa])}!')