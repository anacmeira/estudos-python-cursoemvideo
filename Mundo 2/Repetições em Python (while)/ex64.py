print("=======================[LENDO NÚMEROS INTEIROS] =======================")
cont = n = soma = contador = 0
while cont !=999:
    n = int(input("Digite um número [999 para parar] ::"))
    if n != 999:
     soma +=n
     contador += 1
    else:
       cont = 999
print("~"*80)
print("Você digitou {} números e a soma entre eles foi {}".format(contador,soma))
print("~"*80)
