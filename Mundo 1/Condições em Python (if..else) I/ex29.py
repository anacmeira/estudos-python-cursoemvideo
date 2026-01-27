print("-------------------VERIFICAÇÃO DE SEGURANÇA DAS VIAS BRASILEIRAS-------------------")
kmr = float(input("Informe qual a velocidade do seu carro: "))

if kmr > 80:
    multa = kmr - 80
    print("------------------------------------------------------------------------------------")
    print("VOCÊ FOI MULTADO!")
    print("Você excedeu a velocidade permitida de 80km/k estando a {}km/h".format(kmr))
    print("E está sendo multando no valor de de R$7,00 por cada km excedido.")
    print("Pelos {} kms excedidos você deve pagar uma multa de R${:.2f}".format(multa, multa*7))
    print("------------------------------------------------------------------------------------")
else:
    print("------------------------------------------------------------------------------------")
    print("Você está dentro do limite de velocidade permitido!")
    print("Continue assim..")
    print("------------------------------------------------------------------------------------")
