from random import randint
from time import sleep
from _operator import itemgetter
jogo = {
        'jogador 1': randint(1,6),
        'jogador 2': randint(1,6),
        'jogador 3': randint(1,6),
        'jogador 4': randint(1,6)
}
rank = {}
print('         VALORES SORTEADOS         ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

rank = sorted(jogo.items(), key=itemgetter(1), reverse=True )
print('-='*30)
for i, v in enumerate(rank):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
