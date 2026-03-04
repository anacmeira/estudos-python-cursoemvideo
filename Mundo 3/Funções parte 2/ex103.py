def ficha(nome='',gols=''):
    if nome == "":
        nome = '<desconhecido>'
    if gols == "":
        gols = 0

    print(f'O jogador {nome} fez {gols} gols no campeonato..')
   

#Comando Principal

print('-='*25)
n = str(input('Nome do jogador ::'))
g = str(input('Número de gols marcados ::'))
ficha(n,g)
