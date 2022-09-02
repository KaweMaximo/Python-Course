salario = float(input('Qual é o salario do Funcionario? R$ '))

if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('Salario Antigo: {:.2f}\nSalario Atual: {:.2f}'.format(salario, novo))
