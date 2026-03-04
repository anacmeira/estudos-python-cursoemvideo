def voto(ano):
    idade = 2026 - ano
    if idade < 16:
        print(f'Com {idade} anos. VOTO NEGADO!')
    elif idade >= 16 and idade <=17 or idade > 70:
        print(f'Com {idade} anos. VOTO OPCIONAL!')
    else:
        print(f'Com {idade} anos. VOTO OBRIGATÓRIO!')


#Comando Principal

print('-='*25)
an = int(input('Informe sua data de nascimento ::'))
voto(an)