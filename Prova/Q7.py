def retornaSoma(numero1,numero2):
    soma = numero1+numero2
    return soma
resultado = retornaSoma(retornaSoma(10,20),retornaSoma(30,40))
print("{}".format(resultado))