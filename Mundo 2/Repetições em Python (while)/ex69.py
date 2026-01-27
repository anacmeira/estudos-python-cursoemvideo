idade = conti = contm = conth = 0
while True:
    print("---------CADASTRE UMA PESSOA---------")
    idade = int(input("Informe a idade da pessoa ::"))
    sexo = str(input("Informe o sexo [F/M] ::")).upper()
    while sexo != 'M' and sexo != "F":
            sexo = str(input("Informe o sexo [F/M] ::")).upper()
    if idade > 18:
            conti +=1
    if sexo == 'F':
            if idade < 20:
                contm +=1
    if sexo == 'M':
            conth +=1
    esc = str(input("Deseja continuar [S/N]? ::")).upper()
    while esc != "S" and esc != "N":
            esc = str(input("Deseja continuar [S/N]? ::")).upper()
    print("-"*50)
    if esc == 'N':
           break
print("---------------FIM DO PROGRAMA---------------")
print("No total, {} tem mais de 18 anos".format(conti))
print("Foram cadastrados um total de {} homens".format(conth))
print("Ao todo {} mulheres possuem menos de 20 anos".format(contm))
