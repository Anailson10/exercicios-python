from datetime import date
ano = int(input('que ano quer analisar? COLOQUE 0 PARA ANALIZAR O ANO ATUAL:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} e BISSEXTO'.format(ano))
else:
    print('o ano {} nao e BISSEXTO'.format(ano))