print('-=-'*15)
print('ANALISADOR DE TRIÃNGULOS')
print('-=-'*15)
um = float(input('PRIMEIRO SEGUIMENTO:'))
dois = float(input('SEGUNDO SEGUIMENTO:'))
tres = float(input('TERCEIRO SEGUIMENTO'))
if um + dois > tres:
    podem = input('os seguimentos a cima PODEM FORMAR um triangulo')
else:
    podem = input('os sguimento a cima NÃO PODEM FORMAR um triangulo')
