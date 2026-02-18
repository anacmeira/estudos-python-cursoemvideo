Pessoa = {}
Pessoa['Nome'] = str(input('Nome :'))
ano = int(input('Data de nascimento :'))
Pessoa['Idade'] = 2025 - ano
Pessoa['CTPS'] = int(input('Carteira de trabalho (0 se não tiver) :'))
if Pessoa["CTPS"] != 0:
    Pessoa['Ano-Contratacao'] = int(input('Ano de contratação :'))
    Pessoa['Salario'] = float(input('Salário :R$'))
    Pessoa['Idade-Aposentadoria'] = (Pessoa["Ano-Contratacao"] - ano) + 20
#Calculando hipoteticamente 20 anos de contribuição para se aposentar...
print('-='*30)
for k, v in Pessoa.items():
    print(f'O valor de {k} é {v}')