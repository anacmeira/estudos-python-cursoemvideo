produtos = ('Lápis', 1.50,
            'Borracha', 2.50,
            'Caderno', 15,
            'Mochila', 136.98,
            'Notebook', 2578.99
            )

print('Os produtos são ...')
for pos in range(0,len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}',end='')
    else:
        print(f'R${produtos[pos]: >8}')

