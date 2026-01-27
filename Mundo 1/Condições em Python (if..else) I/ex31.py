print("--------------CALCULANDO O VALOR DA SUA VIAGEM--------------")
dist = float(input("Informe a distância da viagem em [km/h] :"))
if dist <= 200:
    print("------------------------------------------------------------------------------------------------------------")
    calculo = dist*0.50
    print("Ao todo serão percorridos [{}kms]. Logo, valor da passagem será de [R${:.2f}]".format(dist,calculo))
    print("------------------------------------------------------------------------------------------------------------")

else:
    print("------------------------------------------------------------------------------------------------------------")
    calculo = dist * 0.45
    print("Ao todo serão percorridos [{}kms]. Logo, valor da passagem será de [R${:.2f}]".format(dist, calculo))
    print("------------------------------------------------------------------------------------------------------------")
