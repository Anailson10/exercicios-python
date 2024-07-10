a = int(input('primeiro valor:'))
b = int(input('segundo valor:'))
c = int(input('terceiro valor:'))
#verificando quem e menor.
print('o menor valor digitado foi {}'.format(menor))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
    # verificando quem e o maior.
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
 print('o menor valor digitadi foi {}'.format(maior))