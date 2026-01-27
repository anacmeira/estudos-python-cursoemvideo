palavras = ('aprender', 'programar', 'linguagem', 'python',
 'curso', 'gratis', 'estudar', 'praticar',
 'trabalhar', 'mercado', 'programador', 'futuro')

for pal in palavras:
    print(f'Na palavra {pal.upper()} temos:')
    for letra in pal:
        if letra.lower() in 'aeiou':
            print(f'{letra} ' ,end='')