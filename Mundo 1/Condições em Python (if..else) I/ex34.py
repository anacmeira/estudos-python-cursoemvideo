print("--------------------------CALCULANDO AJUSTE SALÁRIAL--------------------------")
sal = float(input("Informe o valor do seu salário:"))
if sal <= 1250.00:
    print("-----------------------------------------------------------")
    print("Seu aumento salárial será de [R${:.2f}]".format(sal*0.15))
    print("Seu novo salário é de [R${:.2f}]".format(sal*1.15))
    print("-----------------------------------------------------------")

else:
    print("-----------------------------------------------------------")
    print("Seu aumento salárial será de [R${:.2f}]".format(sal*0.10))
    print("Seu novo salário é de [R${:.2f}]".format(sal*1.10))
    print("-----------------------------------------------------------")
