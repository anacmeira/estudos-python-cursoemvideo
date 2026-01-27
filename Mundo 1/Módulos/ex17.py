"""print("-------------------------------CALCULANDO HIPOTENUSA-------------------------------")
co = float(input("Informe o comprimento do cateto oposto:"))
ca = float(input("Informe o comprimento do cateto adjacente:"))
h = (((ca*ca) + (co*co))**0.5)
print("A hipotenusa do triangulo retâgulo é {:.2f}".format(h))"""

#OUU
import math
print("-------------------------------CALCULANDO HIPOTENUSA-------------------------------")
co = float(input("Informe o comprimento do cateto oposto:"))
ca = float(input("Informe o comprimento do cateto adjacente:"))
h = math.hypot(co,ca)
print("A hipotenusa do triangulo retâgulo é {:.2f}".format(h))