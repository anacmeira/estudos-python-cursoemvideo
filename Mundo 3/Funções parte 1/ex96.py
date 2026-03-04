def area(l,c):
    area = l*c
    print(f'A área de um terreno {float(l):.2f}x {float(c):.2f} é {area:.2f}m²')

print('       DADOS DE UM TERRENO'       )
print('='*40)
Larg = float(input('Largura :'))
Comp = float(input('Comprimento :'))

area(Larg,Comp)
print('='*40)