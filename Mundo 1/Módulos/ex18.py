import math
ang = float(input("Informe um angulo:"))
print("O seno de {} é {:.2}".format(ang, (math.sin(math.radians(ang)))))
print("O cosseno de {} é {:.2f}".format(ang, math.cos(math.radians(ang))))
print("A tangente de {} é {:.2f}".format(ang, math.tan(math.radians(ang))))