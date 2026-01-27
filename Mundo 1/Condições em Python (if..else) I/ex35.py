print("-----------------------FORMANDO UM TRIÂNGULO-----------------------")
r1 = float(input("Informe um valor para a reta 1:"))
r2 = float(input("Informe um valor para a reta 2:"))
r3 = float(input("Informe um valor para a reta 3:"))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("PARABÉNS. VOCÊ FORMOU UM TRIÂNGULO")

else:
    print("Com os valores das retes informadas é impossível se obter um triângulo")
print("-------------------------------------------------------------------")