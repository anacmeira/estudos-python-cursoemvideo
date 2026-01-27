print("--------------------APROVANDO SEU EMPRÉSTIMO BANCÁRIO--------------------")
vcasa = float(input("Informe qual o valor da casa desejada: R$"))
salario = float(input("Informe seu salário mensal: R$"))
ano = int(input("Informe em quantos anos você pretende quitar totalmente a casa: "))
parcelas = ano * 12
vparcela = vcasa / parcelas

if vparcela < salario*0.30:
    print("-"*100)
    print("PARABÉNS, EMPRÉSTIMO APROVADO")
    print("Você pagará {} parcelas no valor de [R${:.2f}] cada, totalizando o valor total da casa de [R${:.2f}]".format(parcelas, vparcela, vcasa))
    print("-"*100)

else:
    print("-"*100)
    print("EMPRÉSTIMO NEGADO!")
    print("O valor mensal das parcelas excede 30'%' do seu salário mensal")
    print("Para comprar uma casa no valor de [R${:.2f}] em {} anos a prestação seria [R${:.2f}] você teria que ter um salário superior a [R${:.2f}]".format(vcasa, ano, vparcela ,salario))
    print("-"*100)
