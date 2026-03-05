import moeda
from time import sleep
print('-='*25)
num = float(input('Digite um valor ::R$'))
print('========IMPRIMINDO========')
sleep(1)
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'15% a mais de {moeda.moeda(num)} é {moeda.moeda(moeda.aumentar(num))}')
print(f'20% a menos de {moeda.moeda(num)} é {moeda.moeda(moeda.diminuir(num))}')
print('-='*25)

"""Não achei de suma necessidade, trazer os exercícios restantes requeridos nesta parte de módulo, visto que se trata apenas do mesmo execícío sofrendo pequenas melhorias. Não focando em novos conteúdos ainda não vistos anteriormente."""