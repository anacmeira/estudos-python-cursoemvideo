print("=====================[MAIOR E MENOR VALORES]=====================")
cont = n = soma = media = maiorv = 0
menorv = 99999
R = 'S'

while R != 'N':
    n = int(input("Digite um valor:"))
    soma +=n
    cont+=1
    if maiorv < n:
        maiorv = n
    if menorv > n:
        menorv = n
    R = str(input("Deseja continuar[S/N]? ::")).upper()
print("A média entre os {} valores digitados é {:.2f}".format(cont,float(soma/cont)))
print("O maior e o menor valor digitados, são respectivamente: {} e {}".format(maiorv,menorv))
