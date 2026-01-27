print("=================[LENDO NÚMEROS INTEIROS[DESCONSIDERANDO O FLAG]]=================")
cont = n = soma = 0
while True:
    n = int(input("Informe um número inteiro ::"))
    if n == 999:
        break
    cont+=1
    soma +=n
print("A soma dos {} números digitados é {}".format(cont,soma))