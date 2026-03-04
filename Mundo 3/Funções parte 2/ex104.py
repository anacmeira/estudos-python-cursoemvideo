def LeiaInt(txt):
    ok = False
    valor = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO!Digite um número inteiro que seja válido!\033[m')
        if ok:
            break
    return valor

#Comando Principal

n = LeiaInt('Digite um número ::')
print(f'Você digitou o número {n}')