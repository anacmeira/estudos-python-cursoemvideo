print("---------------------COMPARANDO NÚMEROS---------------------")
n1 = int(input("Informe um número inteiro:"))
n2 = int(input("Informe um segundo número inteiro:"))
if n1>n2:
    print("O número {} é maior que o número {}".format(n1,n2))
    print("-"*100)
elif n2>n1:
    print("O número {} é maior que o número {}".format(n2,n1))
    print("-"*100)
else:
    print("Ambos os números digitados {} e {} são iguais:".format(n1,n2))
    print("-"*100)
