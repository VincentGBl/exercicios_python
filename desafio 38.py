import math
n1 = float(input('número 1: '))
n2 = float(input('núemro 2: '))
if n1 == n2:
    print('não existe número maior,os dois são iguais.')
elif n1 > n2:
    print(f'{math.ceil(n1)} é maior que {math.ceil(n2)}')
elif n2 > n1:
    print(f'{math.ceil(n2)} é maior que {math.ceil(n1)}')