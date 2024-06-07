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

for resultado in resultados:
    print(resultado)