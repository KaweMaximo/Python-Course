a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b>a and b>a:
    maior = b
if c>a and c>a:
    maior = c
print('\nO Menor Valor Digitado foi: {}'.format(menor))
print('\nO Maior Valor Digitado foi: {}'.format(maior))
