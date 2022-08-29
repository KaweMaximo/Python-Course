#--- Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

print('Programa para Exibir somente Números Inteiros\n')

num = float(input('---> Digite o Valor: '))
print('---> O Valor Digitado foi {} e sua Porção inteira é {}'.format(num, math.trunc(num)))