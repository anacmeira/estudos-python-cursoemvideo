dados = []
pessoas = []
menorP = 9999999
maiorP = 0
NomemP = ''

NP = int(input('Informe o número de pessoas que deseja cadastrar :'))

for i in range(0,NP):
    print(f'Pessoa {i+1}')
    dados.append(str(input('Nome :')))
    dados.append(float(input('Peso :')))
    print('*'*15)
    pessoas.append(dados[:])
    dados.clear()

for g in pessoas:
    if g[1] > maiorP:
        maiorP = g[1]
    if g[1] < menorP:
       menorP = g[1]
print(f'Ao todo foram cadastradas {NP} pessoas')
print(f'O maior peso cadastrado foi de {maiorP}kg de ', end='')
for p in pessoas:
   if p[1] == maiorP:
       print(f'{p[0]} ',end='')
print(f'O menor peso cadastrado foi de {menorP}kg de ',end='')
for h in pessoas:
   if h[1] == menorP:
       print(f'{h[0]} ',end='')