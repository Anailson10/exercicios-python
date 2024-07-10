v = float(input('qual a distancia da sua viagem?'))
print('voce esta prestes a comecar uma viagem de {}km.'.format(v))
if v <200:
    preço = (v * 0.50)
else:
    distamcia = v>200
    preço = (v*0.45)
print('o preço de sua passagem sera de R${:.2f}'.format(preço))


