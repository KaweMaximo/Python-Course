distancia = float(input('Qual é a Distância da sua Viagem: '))
print('Você está prestes a começar uma Viagem de {}Km.'.format(distancia))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print('E o preço da sua Passagem será de R${:.2f}'.format(preco))