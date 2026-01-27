print("===========[VERIFICANDO SE UM NÚMERO É PRIMO]===========")
num = int(input("Informe um número ::"))
cont = 0

for c in range(1,num+1):
    if num%c == 0:
        cont +=1
        print("[{}] ->".format(c), end="")
    else:
        print("{} ->".format(c), end=" ")

if cont >2:
    print("\nO número {} não é um número [PRIMO], pois foi dividido {} vezes".format(num,cont))
else:
    print("\nO número {} é um número [PRIMO]".format(num))