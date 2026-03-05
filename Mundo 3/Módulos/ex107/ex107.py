import moeda
from time import sleep
print('-='*25)
num = float(input('Digite um valor ::R$'))
print('========IMPRIMINDO========')
sleep(1)
print(f'A metade de {num} é {moeda.metade(num)}')
print(f'O dobro de {num} é {moeda.dobro(num)}')
print(f'15% a mais de {num} é {moeda.aumentar(num)}')
print(f'20% a menos de {num} é {moeda.diminuir(num)}')
print('-='*25)
