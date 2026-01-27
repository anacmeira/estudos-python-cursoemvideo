print("=================[VERIFICANDO SE EXISTE PALÍDROMO]=================")
frase = str(input("Digite uma frase ::")).strip().upper()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = ''

for letras in range(len(juntos)-1, -1, -1):
    inverso += juntos[letras]
print("="*30)
print("[{}] -++++- [{}]".format(juntos,inverso))
if juntos == inverso:
    print("Temos um palíndromo")
else:
    print("Não temos um palíndromo")
print("="*30)
