print("-----------------------[ÍMPAR OU PAR???]-----------------------")
n = int(input("Informe um número inteiro:"))
if n%2 == 0:
    print("--------------------------------")
    print("PAR")
    print("O número {} é par".format(n))
    print("--------------------------------")
else:
    print("--------------------------------")
    print("ÍMPAR")
    print("O número {} é ímpar".format(n))
    print("--------------------------------")
