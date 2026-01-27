ficha = list()
cmd = 0
while True:
    nome = str(input('Nome do Aluno :'))
    n1 = float(input('Nota 1 :'))
    n2 = float(input('Nota 2 :'))
    media = (n1+n2) / 2
    ficha.append([nome,[n1,n2],media])

    resp = str(input('Deseja continuar [S/N] :'))
    if resp in 'Nn':
        break

print('-='*10,'IMPRIMINDO BOLETINS','-='*10)
print(f'{'No'} {'Nome':^15} {'Média':^15}')
print('-'*50)

for i, l in enumerate(ficha):
    print(f'{i} {l[0]:^17} {l[2]:^15.2f}')

while cmd != 999:
    cmd = int(input('Deseja saber as notas de qual aluno : [(999) Para o programa]:'))
    for i, l in enumerate(ficha):
        if cmd == i:
            print(f'As notas de {l[0]} são: {l[1]}')
        
print('-'*50)
print('Obrigada! Volte sempre!')