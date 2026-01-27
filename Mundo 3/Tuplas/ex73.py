times = ('FLAMENGO', 'PALMEIRAS', 'CRUZEIRO', 'MIRASSOL', 'FLUMINENSE',
          'BOTAFOGO', 'BAHIA', 'SÃO PAULO', 'GRÊMIO', 'RED BULL BRAGANTINO', 
          'ATLÉTICO MINEIRO', 'SANTOS', 'CORINTHIANS', 'VASCO DA GAMA', 'VITÓRIA', 
          'INTERNACIONAL', 'CEARÁ', 'FORTALEZA', 'JUVENTUDE', 'SPORT')

print('================CLASSIFICADOS BRASILEIRÃO================')
print(f'Os cinco primeiros colocados são: {times[:5]}')
print(f'Os quatro últimos colocados são: {times[-4:]}')
print(f'Os times em ordem alfabetica são: {sorted(times)}')
print(f'O ATLÉTICO MINEIRO está na {times.index("ATLÉTICO MINEIRO")+1} posição')