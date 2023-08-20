nome = str(input('digite seu nome: '))
media = float(input('digite a média do aluno: '))
sit = ''
if media >= 6:
    sit = 'Aprovado'
else:
    sit = 'Reprovado'
aluno = {'aluno': nome, 'media': media, 'situação': sit}
print(f'o aluno {aluno["aluno"]},teve média {aluno["media"]:.2f} e se encontra {aluno["situação"]}')