from random import randint
nuns = (randint(1,10),randint(1,10),randint(1,10),
        randint(1,10),randint(1,10))
print('Os números sorteados foram :')
for n in nuns:
    print(f'{n} ',end='')
print(f'\nO menor número sorteado foi {min(nuns)}')
print(f'O maior número sorteado foi {max(nuns)}')