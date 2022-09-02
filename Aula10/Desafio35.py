print('~' * 30)
print('Analisador de Triângulo')
print('~' * 30)

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('~' * 30)
    print('Os Segmentos acima PODEM FORMAR Triângulo!')
    print('~' * 30)
else:
    print('~' * 30)
    print('Os Segmentos acima NÃO PODEM FORMAR Triângulo!')
    print('~' * 30)