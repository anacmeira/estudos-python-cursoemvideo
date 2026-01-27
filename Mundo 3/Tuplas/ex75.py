val = (int(input('Informe um valor ::')),
       int(input('Informe um valor ::')),
       int(input('Informe um valor ::')),
       int(input('Informe um valor ::')))

print(f'O valor 9 apareceu {val.count(9)} vezes')
print(f'O número 3 apareceu pela primeira vez na {val.index(3)+1
                                                  }ª posição')
print('Os valores pares foram : ', end='')
for v in val:
    if v % 2 == 0:
        print(f'{v} ',end='')