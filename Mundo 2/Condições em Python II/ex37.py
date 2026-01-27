print("--------------------------------CONVERSÃO DE NÚMEROS--------------------------------")
num = int(input("Informe o número que deseja que seja feita a conversão: "))
print("Informe os números de [1-3]\n [1] - BASE BINÁRIA\n [2] - BASE OCTAL\n [3] - BASE HEXADECIMAL ::" )
print("-------------------------------------------------------------------------------------")
n = int(input("SUA ESCOLHA: "))
if n == 1:
    fnum = f'{num:b}'
    print("O número {} convertido para base binaria é = {}".format(n, fnum))
elif n == 2:
        fnum = f'{num:o}'
        print("O número {} convertido para base octal é = {}".format(n, fnum))
elif n == 3:
    fnum = f'{num:x}'
    print("O número {} convertido para base binaria é = {}".format(n, fnum))
else:
    print("NÚMERO INFORMADO INVÁLIDO!\nVocê deve escolher os números de [1-3] de acordo com o formulário acima!")