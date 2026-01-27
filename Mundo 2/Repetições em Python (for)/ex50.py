print("==============LENDO SEIS NÚMEROS INTEIROS E VENDO SE SÃO PARES")
soma  = 0
contp = 0
conti = 0
for c in range(0,6):
   n = int(input("Informe o valor do {}° número::".format(c+1)))
   if n%2 == 0:
      soma = soma + n
      contp += 1
   else:
    conti = conti + 1
print("="*80)
print("Dentro os números digitados a soma dos [{}] nums pares é [{}]".format(contp,soma))
print("Foram digitados [{}] nums ímpar".format(conti))
print("="*80)
