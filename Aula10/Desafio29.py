velocidade = float(input('Qual é a Velocidade Atual do Carro ?\nR: '))

if velocidade > 80:
    print('-=-' * 20)
    print('MULTADO! Você excedeu o limite permitido que é de 80KM/h')
    multa = (velocidade-80) * 7
    print('Você de pagar uma multa de R${:.2f}!!!'.format(multa))
    print('-=-' * 20)
else:
    print('-=-' * 20)
    print('Tenha um bom dia! Dirija com Segurança')
    print('-=-' * 20)
