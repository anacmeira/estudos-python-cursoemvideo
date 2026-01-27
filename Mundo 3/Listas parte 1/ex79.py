lisVal = []

while True:
    n = int(input('Informe um número ::'))
    if n not in lisVal:
        lisVal.append(n)
        print('Número cadastrado com sucesso')
    else: 
        print('Número já cadastrado anteriormente!')
    r = str(input('Deseja continuar?[S/N]'))
    if r in 'Nn':
        break
lisVal.sort()
print(f'Os números cadastrados foram {lisVal}')