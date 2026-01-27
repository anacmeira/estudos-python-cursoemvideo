matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaP = 0
SomaTP = 0
MV =  0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input((f'Informe o número para posição [{l}, {c}] :')))

print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            somaP += matriz[l][c]
        if matriz[1][c] > MV:
            MV = matriz[1][c]
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
       
print('-='*30)
for l in range(0,3):
        SomaTP += matriz[l][2]

print(f'A soma de todos os valores par é {somaP}')
print(f'A soma de todos os valores  terceira coluna é {SomaTP}')
print(f'O maior valor da segunda linha é {MV}')