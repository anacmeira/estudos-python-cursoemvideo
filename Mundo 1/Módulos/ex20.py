import random
print("--------------------------------SORTEANDO ORDEM DE APRESENTAÇÃO--------------------------------")
n1 = str(input("Informe um nome: "))
n2 = str(input("Informe um segundo nome: "))
n3 = str(input("Informe um terceiro nome: "))
n4 = str(input("Informe um quarto nome: "))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("A ordem de aparesentação será :")
print(lista)