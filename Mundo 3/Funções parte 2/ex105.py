def notas(*notas,sit=False):
    """
      --> Função para analisar as notas e a situação de um aluno.
          :notas - aceita de uma a várias notas
          :sit - se True retornará a situação em que se encontra o aluno
          :return - retorna um dicionário com todas as informações correlacionas as notas informadas

    """
    info = dict()
    info['Quantidade Notas'] = len(notas)
    info['Maior Nota'] = max(notas)
    info['Menor Nota'] = min(notas)
    info['Média da turma'] = ((sum(notas))/ (len(notas)))
    if sit:
        if info['Média da turma'] < 5:
            info['Situação'] = 'RUIM'
        elif info['Média da turma'] > 5 and info['Média da turma'] <=7:
            info['Situação'] = 'BOA'
        else:
            info['Situação'] = 'ÓTIMA'
    return info
    
#Comando Principal

print('-='*25)
resp = notas(4.5,8,10,4.6,9.5, sit=True)
print(resp)
