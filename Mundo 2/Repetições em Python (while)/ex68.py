print("------------[TABUADA]------------")
n = 0
while True:
    n = int(input("Informe um número para calcular a tabuada ::"))
    if n < 0:
     break
    else:
        for c in range(1,11):
           print('~'*15)
           print("[{} x {} = {}]".format(n,c,n*c))
        print("="*60)
print("PROGRAMA TABUADA ENCERRADO! Volte Sempre!")