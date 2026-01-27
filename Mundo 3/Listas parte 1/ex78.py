valores = []
for v in range(0,5):
    valores.append(int(input(f'Informe um valor para a posição {v+1} ::')))

print(f'O maior valor da lista é {max(valores)} na posição {valores.index(max(valores))+1}')
print(f'O menor valor da lista é {min(valores)} na posição {valores.index(min(valores))+1}')
