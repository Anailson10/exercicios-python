from math import hypot
cato = float (input('comprimento do cateto oposto:'))
cata = float (input('cateto adjacente:'))
hi = hypot (cato,cata)
print('a hipotenusa vai medir {:.2f}'.format(hi))