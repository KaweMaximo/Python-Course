frase = str(input('Digite uma Frase: ')).upper().strip()
print('A Letra A parece {} vezes na frase'.format(frase.count('A')))
print('Primeira Letra A se Encontra em {}º Posição'.format(frase.find('A')+1))
print('Ultima Letra A se Encontra na Posição {}ª'.format(frase.rfind('A')+1))