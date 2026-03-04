def BlibFun(Com):
    help(Com)

def titulo(msg, cor=0):
    tam = len(msg)
    print('~'*tam)
    print(msg)
    print('~'*tam)

#Comando Principal
c = ''

while True:
    titulo('SISTEMA DE AJUDA PYHelp')
    c = str(input('Biblioteca Função >'))
    if c.upper() == 'FIM':
        break

    else:
        BlibFun(c)
titulo('ATÉ LOGO!')