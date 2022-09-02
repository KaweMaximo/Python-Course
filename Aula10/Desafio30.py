numero = int(input('Me diga um número Qualquer: '))
resultado = numero % 2

if resultado == 0:
    print('O Numero {} é PAR!'.format(numero))
else:
    print('O Numero {} é IMPAR'.format(numero))