def fatorial(n, show=False):
    fat = 1
    for c in range(n,0,-1):
        if show :
            print(f'{c} ',end='')
            if c > 1:
                print(f'x ',end='')
            else:
                print(f'= ',end='')

        fat *=c
    return fat
        
#Comando Principal

print('-='*25)
num = int(input('Informe um número ::'))
print(fatorial(num,True))