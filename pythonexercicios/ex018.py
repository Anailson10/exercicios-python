import math
print('-'*12)
ang = float (input('digite o angulo q voce deseja:'))
seno = math.sin(math.radians(ang))
print('o angulo de {} graus tem o seno de {:.2f}'.format(ang,seno))
cosseno = math.cos(math.radians(ang))
print('o angulo de {} tem o cosseno de {:.2f}'.format(ang,cosseno))
tangente = math.tan(math.radians(ang))
print('o angulo de {} tem a tangente de {:.2f}'.format(ang,tangente))
print('-'*12)
