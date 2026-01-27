print("===CALCULANDO GASTOS COM TINTA===")
l = float(input("Informe a largura da parede :"))
a = float(input("Informe a altura da parede :"))
a = l*a
gastosT = (a*1)/2
print("Para pintar uma parede com {:.2f}m² será necessário {:.2f} litros de tinta".format(a, gastosT))