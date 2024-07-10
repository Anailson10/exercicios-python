salario = float(input('qual o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('quem ganhava {:.2f} agora ganha {:.2f}'.format(salario, novo))