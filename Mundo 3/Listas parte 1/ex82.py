ValL = []
ValI = []
ValP = []

while True:
    n = int(input('Informe um número :'))

    if n not in ValL:
        ValL.append(n)
    else:
        print('Informe um valor diferente!')
    
    r = str(input('Deseja continuar?[S/N]'))

    if r in 'Nn':
        break
for c in ValL:
    if c % 2 == 0:
        ValP.append(c)
    else:
        ValI.append(c)
print(f'On números informados foram: {ValL}')
print(f'Os números pares informados foram: {ValP}')
print(f'Os números ímpares informados foram:{ValI}')