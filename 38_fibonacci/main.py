"""
Crie um programa onde o usuário informa o número de sequências de Fibonacci a ser calculada.
"""
while True:

    def calcular_fibonacci(n):
        if n <= 1:
            return n
        else:
            return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

    print("Irei mostrar o número da sequências de Fibonacci do valor informado.")
    n = int(input("Informe um número:"))

    for x in range(n):
        print(calcular_fibonacci(x))