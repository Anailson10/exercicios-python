dias=int(input('quantos dias alugado?'))
rodei=int(input('quantos km rodados?'))
diasr=(60*dias) + (0.15*rodei)
print('o total a pagar e de {}R$:'.format(diasr))