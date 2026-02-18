dados = {}
gols = []
i = 0
print('-='*30)
print('          Coletando dados do campeonato       ')
dados['nome'] = str(input('Nome :'))
Npartidas = int(input('Número de partidas jogadas :'))
while i < Npartidas:
    gols.append(int(input(f'Quantos gols foram feitos na partida {i+1}? :')))
    dados['gols'] = gols
    dados['RedimentoT'] = sum(dados["gols"])
    i+=1
print('='*45)
print(dados)
print('='*45)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('='*45)
print(f'O jogador {dados["nome"]} jogou ao todo {Npartidas} partidas')
print('='*45)
for c in range(0,len(gols)):
    print(f'--> Partida {c+1}: {gols[c]} gols')
print(f'Ao todo foram marcados {dados["RedimentoT"]} gols')
print('='*45)
