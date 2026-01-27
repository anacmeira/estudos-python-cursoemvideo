lista = ('ZERO', 'UM', 'DOIS', 'TRÊS', 
         'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 
         'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 
         'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
num = int(input('Informe um número de [0-20] ::'))
for n in range(0,len(lista)):
    if n == num:
        print(f'Você digitou o número {lista[n]}')
