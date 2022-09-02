from random import randint
import time

print('-=-' * 20)
computador = randint(0,5)
print('Vou pensar em um número entre 0 e 5. Tende Adivinhar...')
print('\nPROCESSANDO...')
print('-=-' * 20)
time.sleep(5)

jogador = int(input('Em que número eu Pensei ?\nR: '))

if jogador == computador:
    print('-=-' * 20)
    print('PARABÉNS! Você Ganhou !!!')
    print('-=-' * 20)
else:
    print('-=-' * 20)
    print('GANHEI! Pensei no Número {} e não no {}'.format(computador,jogador))
    print('-=-' * 20)
