print("================[LENDO A DATA DE NASCIMENTO DE SETE PESSOAS]")
cont = 0
for c in range(0,7):
    data = int(input("Informe a data de nascimento da {}° pessoa ::".format(c+1)))
    MI = 2025 - data
    if MI >= 18:
        cont +=1
print("No ano de 2025 das sete pessoas {} atigiram a maior idade e {} ainda são menores:".format(cont,7-cont))