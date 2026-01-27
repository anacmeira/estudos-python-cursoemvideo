print("-------------------------------------[CALCULANDO SEU IMC]-------------------------------------")
peso = float(input("Informe seu peso em (kg):"))
altura = float(input("Informe sua altura em (m) :"))
imc = peso / (altura*altura)

if imc <18.5:
    print("[ABAIXO DO PESO!]")
    print("O seu [IMC] foi de {:.2f} e você está abaixo do peso indicado..".format(imc))

elif imc >=18.5 and imc <=25:
    print("[PESO IDEAL!]")
    print("O seu [IMC] foi de {:.2f} e você está no peso ideal..".format(imc))

elif imc >25 and imc <=30:
    print("[SOBREPESO!]")
    print("O seu [IMC] foi de {:.2f} e você está com sobrepeso..".format(imc))

elif imc >30 and imc <=40:
    print("[OBESIDADE!]")
    print("O seu [IMC] foi de {:.2f} e você está com obesidade..".format(imc))

else:
    print("[OBESIDADE MÓRBIDA!]")
    print("O seu [IMC] foi de {:.2f} e você está com obesidade mórbida..".format(imc))
