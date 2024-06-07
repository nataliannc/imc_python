#yield 
def calcular_tabuada(x,y):
    soma = x + y
    yield soma
    subtracao = x - y
    yield subtracao
    multiplicacao = x * y
    yield multiplicacao
    divisao = x / y
    yield divisao

x = int(input("Informe o primeiro número:"))
y = int(input("Informe o segundo número:"))

resultados = calcular_tabuada(x,y)

#o comando next faz com que a função chame o proxímo retorno
print(f"A soma é {next(resultados)}.")
print(f"A subtração é {next(resultados)}.")
print(f"A multiplicação é {next(resultados)}.")
print(f"A divisão é {next(resultados)}.")