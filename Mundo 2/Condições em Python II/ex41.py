print("--------------------------------------------[CATEGORIA DO ATLETA]--------------------------------------------")
ano = int(input("Informe sua data de nascimento :"))
idade = 2025 - ano
print("-"*100)
if idade <=9:
    print("O atleta possui {} anos e está na categoria [MIRIM]".format(idade))

elif idade >=10 and idade <=14:
    print("O atleta possui {} anos e está na categoria [INFANTIL]".format(idade))

elif idade >=15 and idade <=19:
    print("O atleta possui {} anos e está na categoria [JUVENIL]".format(idade))

elif idade >=20 and idade <=25:
    print("O atleta possui {} anos e está na categoria [SÊNIOR]".format(idade))

else:
    print("O atleta possui {} anos e está na categoria [MASTER]".format(idade))

print("-"*100)