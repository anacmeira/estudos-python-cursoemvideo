from random import randint
from time import sleep
nums = list()

def sorteio(list=[]):
    print('           SORTEANDO NÚMEROS           ')
    print('~-='*20)
    for c in range(0,5):
        list.append(randint(0,10))
    print('Os números sortedos foram :: ',end='')
    for d in list:
        print(f'{d} ',end='',flush=True)
        sleep(1)
    print('<<<PRONTO<<<')

def SomaPar(lista=[]):
    soma = 0
    print('           SOMANDO NÚMEROS           ')
    print('~-='*25)
    print(f'A soma entre os valores pares dos números sorteados {lista} é ::',end='')
    for c in lista:
        if c % 2 == 0:
            soma+= c
    print(soma)

sorteio(nums)
sleep(2)
SomaPar(nums)