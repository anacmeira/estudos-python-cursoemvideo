aluno = {}
aluno['nome'] = str(input('Nome :'))
aluno['nota'] = float(input(f'Média de {aluno["nome"]} :'))

if aluno["nota"] >= 6:
    aluno['situacao'] = 'APROVADO(A)'
else:
    aluno['situacao'] = 'REPROVADO(A)'

for K, v in aluno.items():
    print(f'{K} é igual a {v}')