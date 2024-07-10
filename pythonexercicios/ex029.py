car = float(input('qual a velocidade atual de um carro?'))
if car > 80:
    print('MULTADO voce excedeu a velocidade permitida que e de 80km/hr')
    multa = (car-80) * 7
    print('voce deve pagar uma multa de R${:.2f} '.format(multa))
print('tenha um bom dia e dirija com seguramça!')
