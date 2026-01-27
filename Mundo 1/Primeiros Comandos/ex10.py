print("CONVERSOR DE MOEDAS")
d = float(input("Informe quanto en dinheiro você possui na sua conta: R$"))
c = d/5.44
e = d/6.37
print("Com o valor informado R${:.2f} você pode comprar $${:.2f} e €{:.2f}".format(d,c,e))