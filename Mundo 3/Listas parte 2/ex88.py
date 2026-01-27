from random import randint
from time import sleep
lista = []
jogos = []
tot = 1
print('*='*30)
print('      JOGUE NA MEGA-SENA    ')
print('*='*30)

Jog = int(input('Quantos jogos deseja fazer ?:'))
while tot <= Jog:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'**************** IMPRIMINDO {Jog} JOGOS ****************')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1} -> {l}')
    sleep(2)
print('*='*30)
print('Good Luck!')
