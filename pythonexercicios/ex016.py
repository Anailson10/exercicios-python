from math import trunc
#opçao 1
'''fracionada = float (input('digite um valor:'))
inteira= int (fracionada)
print('o valor digitado foi de {} e a sua porcao inteira e {} '.format(fracionada,inteira))'''

#ou pode se usar 'math.trunc' ex:fracionada,math.trunc(fracionada)

#opçao 2
num= float (input('digite um numero:'))
print('o valor digitado foi {} e a sua porcao inteira e {} '.format(num,trunc(num)))