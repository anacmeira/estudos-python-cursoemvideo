import random
print("------------------------------JOGO DE ADIVINHAÇÃO------------------------------")
n = int(input("Informe um número de [0-5] :"))
n1 = str(n)
lista = ['0','1','2','3','4','5']
escolha = random.choice(lista)
if n1 == escolha:
    print("-------------------------------------------------------------------------------")
    print("PARABÉNS!!")
    print("Você escolheu o número {} mesmo número escolhido pelo computador".format(n1))
    print("-------------------------------------------------------------------------------")
else:
    print("-------------------------------------------------------------------------------")
    print("PERDEU!!")
    print("Você digitou o número {} e o número escolhido pelo computador foi {}".format(n1, escolha))
    print("-------------------------------------------------------------------------------")
