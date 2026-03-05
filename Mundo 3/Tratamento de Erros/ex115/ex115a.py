
def menuP():
    print('--'*20)
    print('             MENU PRINCIPAL       ')
    print('--'*20)
    print(f'{'\033[0;32m1\033[m'} {'\033[0;31m-\033[m':^2} {'\033[0;34mVer pessoas cadastradas\033[m':^4}')
    print(f'{'\033[0;32m2\033[m'} {'\033[0;31m-\033[m':^2} {'\033[0;34mCadastrar nova pessoa\033[m':^4}')
    print(f'{'\033[0;32m3\033[m'} {'\033[0;31m-\033[m':^2} {'\033[0;34mSair do sistema\033[m':^4}')
    print('--'*20)

def EscolhendoOp(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError,TypeError):
            print('\033[0;31mERRO!Digite um número inteiro que seja válido!\033[m')
            continue
        else:
            if n == 1:
                print('--'*20)
                print('            PESSOAS CADASTRADAS')
                print('--'*20)
                break
            elif n == 2:
                print('--'*20)
                print('                OPÇÃO 2')
                print('--'*20)
                break
            elif n == 3:
                break
            else:
                print('\033[0;31mERRO!Digite um número inteiro de acordo com o menu!\033[m')
    return n


#programa principal

while True:
    menuP()
    n = EscolhendoOp('\033[0;36mSua escolha ::\033[m')
    if n == 3:
        break
print('Obrigada')