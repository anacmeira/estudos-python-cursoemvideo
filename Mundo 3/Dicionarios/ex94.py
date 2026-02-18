galera = list()
pessoas = dict()
mulheres = list()
PAM = list()
cont = 0
Midade = 0
while True:
    pessoas.clear
    pessoas['nome'] = str(input('Informe o nome :'))
    while True:
        pessoas['sexo'] = str(input('Informe o sexo [M/F] :')).upper()[0]
        if pessoas["sexo"] in 'MF':
            break
        print('ERRO!! Favor responder com [M/F]')
    if pessoas["sexo"] == 'F':
        mulheres.append(pessoas["nome"])
    pessoas['idade'] = int(input('Informe a idade :'))
    Midade += pessoas["idade"]
    galera.append(pessoas.copy())
    cont += 1
    while True:
        resp = str(input('Deseja Continuar [S/N] :')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!! Informe apenas [S/N]')
    if resp == 'N':
        break
    print('-='*30)
print('='*90)
print('               IMPRIMINDO DADOS               ')
print(f'Ao todo foram cadastradas {cont} pessoas')
print(f'A média de idades cadastradas é igual a {Midade/cont:.2f}')
print('As mulheres cadastradas foram ',end="")
for m in mulheres:
    print(f'{m},' , end=" ")
print()
print('As pessoas cadastradas que possuem idade acima da média são')
for c in galera:
    if c["idade"] >= (Midade/cont):
        print('      ')
        for k, v in c.items():
            print(f'{k} = {v} ',end='')
        print()
print('='*90)
print('<<<ENCERRADO<<<')