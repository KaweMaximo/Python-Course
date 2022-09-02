n = str(input('Digite seu Nome Completo: ')).strip()
nome = n.split()
print('Seu Primeiro nome é : {}'.format(nome[0]))
print('Seu Ultimo Nome é : {}'.format(nome[len(nome)-1]))
