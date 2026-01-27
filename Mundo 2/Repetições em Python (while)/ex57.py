print("==================[VERIFICANDO O SEXO DE UMA PESSOA]==================")
sexo = ""
while sexo != "M" and sexo != "F":
    sexo = str(input("Informe o sexo [M-F]")).upper()
    if sexo != "F" and sexo != "M":
        print("Informe o sexo corretamente!")
print("ACABOU")