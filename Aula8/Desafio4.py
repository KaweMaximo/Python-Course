# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

n1 = str(input('Digite o Nome do Primeiro Aluno: '))
n2 = str(input('Digite o Nome do Segundo Aluno: '))
n3 = str(input('Digite o Nome do Terceiro Aluno: '))
n4 = str(input('Digite o Nome do Quarto Aluno: '))

lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print('\nO Aluno Escolhido Foi: {}'.format(escolhido))