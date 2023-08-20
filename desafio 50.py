contador = 0
soma = 0
num = 0
for n in range(1, 6 + 1):
   num = int(input(f'me fale o {n} valor:'))
   if num % 2 == 0:
       soma = soma + num
       contador = contador + 1
print(f'somamos {contador} valores e deu {soma}')

