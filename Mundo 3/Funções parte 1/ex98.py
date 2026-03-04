import time
def contador(ini,fim,meio):
    if ini < fim:
        if meio > 0:
            print('~-='*20)
            print(f'Contagem de {ini} até {fim-1} de {meio} em {meio}')
            for i in range(ini,fim,meio):
                print(f'{i} ',end="",flush=True)
                time.sleep(1)
            print('FIM!')
        else:
            print('~-='*20)
            print(f'Contagem de {ini} até {fim-1} de {abs(meio)} em {abs(meio)}')
            for i in range(ini,fim,abs(meio)):
                print(f'{i} ',end="",flush=True)
                time.sleep(1)
            print('FIM!')

    else:
        if meio > 0:
            print('~-='*20)
            print(f'Contagem de {ini} até {fim} de {meio} em {meio}')
            for i in range(ini,fim-1,-meio):
                print(f'{i} ',end="",flush=True)
                time.sleep(1)
            print('FIM!')
        else:
            print('~-='*20)
            print(f'Contagem de {ini} até {fim} de {abs(meio)} em {abs(meio)}')
            for i in range(ini,fim-1,-(abs(meio))):
                print(f'{i} ',end="",flush=True)
                time.sleep(1)
            print('FIM!')

contador(0,11,1)
time.sleep(2)
contador(10,0,2)
time.sleep(2)
print('Sua vez de personalizar a contagem!')
I = int(input('Início :'))
F = int(input('Fim :'))
M = int(input('Passo :'))
contador(I,F,M)