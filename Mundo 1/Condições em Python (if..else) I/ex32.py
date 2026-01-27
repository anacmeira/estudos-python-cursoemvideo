print("------------[ANALISANDO ANOS]------------")
ano = str(input("Informe o ano em questão: "))
dias = str(input("Informe quantos dias possui o ano de {} ao todo:".format(ano)))

if int(dias) == 366 :
    print("-----------------------------------------------------------")
    print("BISSEXTO")
    print("O ano de {} é um bissexto com {} dias".format(ano, dias))
    print("-----------------------------------------------------------")

else:
    print("-----------------------------------------------------------")
    print("O ano de {} é um ano normal com {} dias".format(ano, dias))
    print("-----------------------------------------------------------")
