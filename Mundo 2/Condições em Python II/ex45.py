import random
print("==================================[JOKENPÔ]==================================")
lista = ["pedra", "papel", "tesoura"]
escolha = random.choice(lista)
print("===========PARA JOGAR COM O COMPUTADOR ESCOLHA UMA DAS OPÇÕES ABAIXO")
print("[PEDRA]")
print("[PAPEL]")
print("[TESOURA]")
print("="*80)
jok = str(input("SUA ESCOLHA :")).strip()
jok = jok.lower()

print("="*80)
if jok == "pedra":
    if escolha == "papel":
        print("VOCÊ PERDEU!")
        print("Papel embrulha pedra!")
    elif escolha == "tesoura":
        print("VOCÊ GANHOU!")
        print("Pedra esmaga tesoura!")
    else:
        print("HOUVE EMPATE!")
        print("Pedra com pedra ihulll!!")

elif jok == "papel":
    if escolha == "tesoura":
        print("VOCÊ PERDEU!")
        print("Tesoura corta papel!")
    elif escolha == "pedra":
        print("VOCÊ GANHOU!")
        print("Papel embrulha pedra!")
    else:
        print("HOUVE EMPATE!")
        print("Papel com papel ihull!!")

elif jok == "tesoura":
    if escolha == "pedra":
        print("VOCÊ PERDEU!!")
        print("Pedra esmaga tesoura!")
    elif escolha == "papel":
        print("VOCÊ GANHOU")
        print("Tesoura corta papel!")
    else:
        print("HOUVE EMPATE!")
        print("Tesoura com tesoura, ihulll!!")

else:
    print("OPÇÃO INFORMADA INVÁLIDA")