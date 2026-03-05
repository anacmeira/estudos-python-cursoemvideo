"""Já havia inderido a validação requerida no ex114, no ex 113. Logo, ambos são indênticos!"""
def LeiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError,TypeError):
            print('\033[0;31mERRO!Digite um número inteiro que seja válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mERRO!O usuário preferiu não informar o número!\033[m')
            return 0
        else:
            return n
        
def LeiaFloat(txt):
    while True:
        try:
            n = float(input(txt))
        except (ValueError,TypeError):
            print('\033[0;31mERRO!Digite um número real que seja válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO!O usuário preferiu não informar o número!\033[m')
            return 0
        else:
            return n
#Comando Principal

i = LeiaInt('Digite um número inteiro ::')
print(f'Você digitou o número {i}')

r = LeiaFloat('Digite um número real ::')
print(f'Você digitou o número {r}')