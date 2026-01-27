print("=============[CALCULANDO OS 10 PRIMEIROS TERMOS DE UMA PA]=============")
t1 = int(input("Informe o primeiro termo da PA ::"))
RA = int(input("Informe a razão da PA ::"))
UPA = t1 + (10-1)*RA
for c in range(t1,UPA+1,RA):
    print("[{}]->".format(c), end=" ")
print("FIM")