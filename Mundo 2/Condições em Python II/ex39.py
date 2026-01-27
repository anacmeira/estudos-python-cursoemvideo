print("----------------------------------[ALISTAMENTO MILITAR]----------------------------------")
nome = str(input("Informe seu nome completo:")).strip()
data = int(input("Informe sua data de nascimento "))
alistamento = 2025 - data
if alistamento == 18:
    print("É HORA DE SE ALISTAR!")
    print("Olá {}, você tem exatos 18 anos e está na hora de se alistar".format(nome))
elif alistamento < 18:
    print("Seu Alistamento será em {}".format(data+18))
    print("VOCÊ AINDA IRÁ SE ALISTAR!")
    print("Olá {}, ainda não é hora de se alistar, você  está com {} anos e ainda faltam {} anos para o alistamento".format(nome, alistamento,((alistamento-18)*-1)))

else:
    print("Seu Alistamento foi em {}".format(data+18))
    print("PASSOU DA DATA DE ALISTAMENTO!")
    print("Olá {}, você está com {} anos e está {} anos atrasado para o alistamento".format(nome,alistamento,(alistamento-18)))
