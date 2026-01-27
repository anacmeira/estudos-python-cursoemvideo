print("=====================[LENDO O FATORIAL DE UM NÚMERO]=====================")
n = int(input("Informe o número que seja calcular o fatorial ::"))
f = 1
print("Calculando o fatorial de [{}!".format(n), end="")
while n > 0:
    print("{}".format(n), end="")
    print("x" if n > 1 else "=", end="")
    f *=n
    n -=1
print("{}]".format(f), end="")