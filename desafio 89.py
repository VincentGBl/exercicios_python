alunmask = list()
dadalunos = list()
while True:
    alunmask.append(str(input('seu nome por favor: ')))
    alunmask.append(float(input('1 nota: ')))
    alunmask.append(float(input('2 nota: ')))
    alunmask.append(float((alunmask[1] + alunmask[2]) / 2))
    dadalunos.append(alunmask[:])
    alunmask.clear()
    perg = str(input('colocar mais algum aluno?: ')).strip().upper()
    if perg in 'N':
        break
for p in range(len(dadalunos)):
    print(f'{p} {dadalunos[p][0]} -> notas: {dadalunos[p][1]} - {dadalunos[p][2]} -> média: {dadalunos[p][3]}')
while True:
    pergs = int(input('mostrar as notas de qual aluno?(999 interrompe): '))
    if pergs == 999:
        break
    print(f'as notas de {dadalunos[pergs][0]} -> {dadalunos[pergs][1]} - {dadalunos[pergs][2]} ')
