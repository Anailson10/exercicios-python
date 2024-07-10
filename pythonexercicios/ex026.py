n = str(input('digite uma frase:')).upper().strip()
print('a letra A aparece {} vezes na frase'.format(n.count('A')))
print('a primeira letra A apareceu na posiçao {}'.format(n.find('A')+1))
print('a ultima letra A apareceu na posicao {}'.format(n.rfind('A')+1))
