from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador 'sortear'
print('-=-' * 20)
print('vou pensar em um numero entre 0 e 5 tente adivinhar!')
print('-=-' * 20)
jogador = int(input('em q numero eu pensei?')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('parabens! voce conseguiu me vencer.')
else:
    print('eu ganhei! eu pensei no numero {} e nao no {}.'.format(computador,jogador))



