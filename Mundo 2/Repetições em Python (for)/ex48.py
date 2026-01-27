print("=======[Nums impares e divisores de 3 entre [1-500]]=======")
soma = 0
cont = 0
for c in range(1,501,2):
    if c%3 == 0:
        soma = soma + c
        cont += 1
print("="*60)
print(" A soma dos [{}] números ímpares é = [{}]".format(cont,soma))
print("="*60)
