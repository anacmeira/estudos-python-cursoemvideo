print("=====================[OPERAÇÕES COM DOIS NÚMEROS E MENU]=====================")
n = 0
n1 = int(input("Informe um número ::"))
n2 = int(input("Informe um segundo número ::"))
while  n != 5:
    print("[1]somar")
    print("[2]multiplicar")
    print("[3]maior")
    print("[4] maior número")
    print("[5] sair do programa")
    n = int(input("Sua escolha ::"))
    if n == 1:
        print("="*80)
        print("A soma entre {} e {} é {}".format(n1,n2,n1+n2))
        print("="*80)

    elif n == 2:
        print("="*80)
        print("A multiplicação entre {} e {} é {}".format(n1,n2,n1*n2))
        print("="*80)

    elif n == 3:
        print("="*80)
        print("O maior número entre {} e {} é {}".format(n1,n2,max(n1,n2)))
        print("="*80)

    elif n == 4:
        print("="*80)
        n1 = int(input("Informe um número ::"))
        n2 = int(input("Informe um segundo número ::"))
        print("="*80)

    else:
        print("="*80)
        print("Número digitado [INVÁLIDO]")
        print("Favor escolher um número conforme o menu!")
        print("="*80)

print("FIM")