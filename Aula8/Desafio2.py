# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

print('Programa para Calcular Comprimento do Cateto oposto e do Cateto Adjacente')

co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))

hi = (co ** 2 + ca ** 2) ** (1/2)

print('A Hipotenusa vai medir: {}'.format(hi))