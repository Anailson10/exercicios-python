from random import shuffle
al1 = input('primeiro aluno:')
al2 = input('segundo aluno:')
al3 = input('trceiro aluno:')
al4 = input('quarto aluno:')
lista = [al1,al2,al3,al4]
shuffle(lista)
print('a ordem sorteada sera ')
print(lista)