soma = 0
maisv = 0
cont = 0
for c in range(0,4):
    print("#"*50)
    nome = str(input("Informe o nome da {}° pessoa ::".format(c+1))).strip()
    idade = int(input("Informe agora a idade da pessoa ::"))
    sexo = str(input("Informe o sexo [M-F] da pessoa ::")).strip().upper()
    soma = soma + idade
    if sexo == "M":
        if maisv <idade:
            maisv = idade
            nomev = nome

    elif sexo == "F":
        if idade < 20:
            cont = cont + 1
    else:
        print( "Sexo informado [INVÁLIDO]!")
print("="*50)
print("A média de idades do grupo é {:.2f}".format(float(soma/4)))
print("O nome do homem mais velho é {}".format(nomev))
print("Ao todo {} mulheres tem menos de 20 anos".format(cont))
print("="*50)
