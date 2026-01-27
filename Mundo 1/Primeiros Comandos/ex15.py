d = int(input("Informe o número de dias pelo qual o carro foi alugado :"))
km = float(input("Informe quantos kms já foram rodados :"))
total = (60*d) + (0.15*km)
print("O valor total a se pagar é de R${:.2f}".format(total))