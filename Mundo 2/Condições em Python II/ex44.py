print("========================================[CALCULANDO POSSÍVEIS FORMAS DE PAGAMENTO]========================================")
valor = float(input("Informe o valor a ser pago pelo produto :R$"))
print("Escolha uma das opções..")
print("[1] - À vista(dinheiro/cheque)")
print("[2] - À vista(no cartão)")
print("[3] - Em até(2x no cartão)")
print("[4] - Em(3x ou mais no cartão)")
n = int(input("Sua escolha ::"))
print("="*80)
if n == 1:
    print("Produto pago à vista, recebendo 10'%' de desconto")
    print("Valor inicial do produto [R${:.2f}] valor final a ser pago [R${:.2f}]".format(valor,valor*0.9))

elif n == 2:
    print("Produto pago à vista, no cartão, recebendo 5'%' de desconto")
    print("Valor inicial do produto [R${:.2f}] valor final a ser pago [R${:.2f}]".format(valor,valor*0.95))

elif n==3:
    print("Produto pago em 2x no cartão")
    print("O produto será parcelado em 2x no valor de [R${:.2f}] cada".format((valor/2)))
    print("Valor inicial do produto [R${:.2f}] valor final a ser pago [R${:.2f}]".format(valor,valor))

elif n==4:
    p = int(input("Quantas parcelas :"))
    print("Produto pago em 3x ou mais, no cartão, 20'%' de juros")
    print("O produto será parcelado em {}x no valor de [R${:.2f}] cada".format(p,((valor*1.2)/p)))
    print("Valor inicial do produto [R${:.2f}] valor final a ser pago [R${:.2f}]".format(valor,valor*1.2))

else:
    print("Forma de pagamento inválida!!")
print("="*80)