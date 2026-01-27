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
lisVal.sort(reverse=True)
print(f'Ao todo, foram digitados {len(lisVal)} números')
print(f'Os números cadastrados em ordem decrescente foram foram {lisVal}')
if 5 in lisVal:
    print('O valor 5 está presente na lista')
else:
    print('O valor 5 não está presente na lista')