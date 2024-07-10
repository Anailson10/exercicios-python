preço=float(input('qual e o preço do produto?'))
desconto=float(preço*25/100)
desconto2=float (preço-desconto)
print('o produto que custava {} com o desconto de 25p% vai custar {}'.format(preço,desconto2))