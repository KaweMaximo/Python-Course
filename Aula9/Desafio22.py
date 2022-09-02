import time

nome = str(input('Digite seu Nome Completo: ')).strip()
print('\n')
print('Analizando seu Nome...')
print('\n')
time.sleep(3)
print('\n')
print('Seu nome em Maiúscula é : {}'.format(nome.upper()))
print('Seu nome em Minúscula é : {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))

print('Seu Primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
print('Seu Primerio nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))