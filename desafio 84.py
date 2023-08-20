pessoas = list()
dados = list()
maior = menor = 0
while True:
    pessoas.append(str(input('Qual é o seu nome: ')))
    pessoas.append(int(input('qual é o seu peso: ')))
    if pessoas[1] == 0:
        maior = menor = pessoas[1]
    else:
        if maior < pessoas[1]:
            maior = pessoas[1]
        if menor > pessoas[1]:
            menor = pessoas[1]
    dados.append(pessoas[:])
    pessoas.clear()
    perg = str(input('Colocar mais pessoas?\nS/N : ')).strip().upper()
    if perg in 'N':
        break
print(f'foram cadastradas {len(dados)} pessoas')
print(f'as mai(s) pesada(s) tem {maior} kilos ', end='')
for p in dados:
    if p[1] == maior:
        print(p[0])
print()
print(f'a(s) mais leve(s) pesaram {menor} kilos', end='')
for p in dados:
    if p[1] == menor:
        print(p[0])
