import random
print("==================[JOGO DE ADIVINHAÇÃO 2.0]]==================")
n = 0
cont = 0
nf = 0
lista = ["1","2","3","4","5"]
escolha = random.choice(lista)
print("Jogo de Adivinhação!! Escolha um número entre [1-5]")
while n != escolha:
    n = int(input("Sua escolha ::"))
    n = str(n)
    if n != escolha:
        print("Você errou!")
        print("Informe novamente um número entre [1-5]")
        cont = cont + 1
    else:
        nf = n
print("="*90)
print("VOCÊ ACERTOU!!")
print("Na {} tentativa".format(cont+1))
print("Você digitiou o número {} e o computador escolheu o número {}".format( nf, escolha))
print("="*90)