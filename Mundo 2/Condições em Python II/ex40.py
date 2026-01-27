print("--------------------------------------[CALCULANDO SUA MÉDIA]--------------------------------------")
nome = str(input("Informe seu nome completo :")).strip()
n1 = float(input("Informe sua primeira nota :"))
n2 = float(input("Informe sua segunda nota :"))
media = (n1+n2)/2

if media < 5:
    print("-"*100)
    print("REPROVADO(A)!")
    print("Olá {}, sua média foi de {:.2f}, abaixo de 5".format(nome, media))
    print("Estude mais da próxima!")
    print("-"*100)
elif media > 5 and media <= 6.9:
    print("-"*100)
    print("RECUMPERAÇÃO!")
    print("Olá {}, sua média foi de {:.2f} e você está de recumperação...".format(nome, media))
    print("Estude para a recumperação!..")
    print("-"*100)

else:
    print("-"*100)
    print("APROVADO(A)!")
    print("Olá {} sua média foi de {:.2f} e você está aprovado(a)".format(nome,media))
    print("Parabéns!!")
    print("-"*100)
