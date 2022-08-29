# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = str(input('Digite o Nome do Primeiro Aluno: '))
n2 = str(input('Digite o Nome do Segundo Aluno: '))
n3 = str(input('Digite o Nome do Terceiro Aluno: '))
n4 = str(input('Digite o Nome do Quarto Aluno: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('\nA Sequencia da Apresentação Será: {}'.format(lista))