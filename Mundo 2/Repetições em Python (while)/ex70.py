print("====================[CENTRAL DE PRODUTOS]====================")
total = cont = 0
menorp = 99999
while True:
    print("-------CADASTRE UM PRODUTO-------")
    nome = str(input("Nome do produto ::")).strip()
    while len(nome) == 0:
        nome = str(input("Nome do produto ::")).strip()
    preco = str(input("Preço do produto ::R$")).strip()
    while len(preco) == 0:
        preco = str(input("Preço do produto ::R$")).strip()
    total += float(preco)
    if float(preco) > 1000:
        cont+= 1
    if menorp > float(preco):
        menorp = float(preco)
        nomeMp = nome
    esc = str(input("Deseja cadastrar mais produtos[S/N]? ::")).upper()
    while esc != 'N' and esc != 'S':
        esc = str(input("Deseja cadastrar mais produtos[S/N]? ::")).upper()
    if esc == 'N':
        break
print("~"*60)
print("O gasto total na compra foi de [R${:.2f}]".format(total))
print("No total, {} custam mais que R$1000".format(cont))
print("O nome do produto mais barato é {}".format(nomeMp))
print("~"*60)
