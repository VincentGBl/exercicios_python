r1 = int(input('reta 1: '))
r2 = int(input('reta 2: '))
r3 = int(input('reta 3: '))
#primeira situação
rmai = r1
rmen1 = r2
rmen2 = r3
#segunda situação
if r2 > r1 and r2 > r3:
    rmai = r2
    rmen1 = r1
    rmen2 = r3
#terceira situação
if r3 > r1 and r3 > r2:
    rmai = r3
    rmen1 = r2
    rmen2 = r1
if rmen1 + rmen2 > rmai:
    print('sim pode ser um triangulo')
else:
    print('não,não da para ser um triângulo')
