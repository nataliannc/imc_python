"""
Crie um programa que o usuário possa escolher se deseja saber a área de um círculo, de um triângulo ou de um trapézio.
"""

def exibir_menu():
    print("Digite 1 para calcular a área de um círculo.")
    print("Digite 2 para calcular a área de um triângulo.")
    print("Digite 3 para calcular a área de um trapézio.")
    print("Digite 4 para sair do programa")

def calcular_circulo(raio):
    circulo = (raio**2) * 3.14
    return circulo

def calcular_triangulo(base_circulo, altura_triangulo):
    triangulo = (base_circulo * altura_triangulo)/2
    return triangulo

def calcular_trapezio(base1, base2, altura_trapezio):
    trapezio = (base1 + base2) * altura_trapezio/2
    return trapezio


while True:
    exibir_menu()
    opcao = input("Qual área você deseja calcular:")

    if opcao == "1":
        raio = int(input('Informe a base do cículo:'))
        print(f'A área do círculo é {calcular_circulo(raio)}')
    elif opcao == "2":
        base_circulo = int(input("Informe o valor da base do triângulo:"))
        altura_triangulo = int(input("Informe o valor da altura do triângulo:"))
        print(f'A área do triângulo é {calcular_triangulo(base_circulo, altura_triangulo)}')
    elif opcao == "3":
        base1 = int(input("Informe o valor da primeira base do trapézio:"))
        base2 = int(input("Informe o valor da segunda base do trapézio:"))
        altura_trapezio = int(input("Informe o valor da altura do trapézio:"))
        print(f'A área do trapézio é {calcular_trapezio(base1, base2, altura_trapezio)}')
    else:
        print("Opção invalida!")