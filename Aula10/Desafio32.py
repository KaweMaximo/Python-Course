from datetime import date

ano = int(input('Que ano Deseja Analisar ? --> Coloque 0 para Analisar o Ano Atual <---\nR: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O Ano {} é BISSEXTO'.format(ano))
else:
    print('O Ano {} NÃO é BISSEXTO'.format(ano))