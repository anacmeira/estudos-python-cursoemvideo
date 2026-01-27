print("====================[ANALISANDO O MAIOR E MENOR PESO ENTRE CINCO PESSOAS]====================")
lista = [5]
menorp = 999999
maiorp = 0
for c in range(0,5):
    peso = float(input("Informe o peso da {}° pessoa ::".format(c+1)))
    if menorp > peso:
        menorp = peso
    if maiorp < peso:
        maiorp = peso

print("\nDentre os pesos informados o menor peso é [{}] e o maior [{}]".format(menorp,maiorp))