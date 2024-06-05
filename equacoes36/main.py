"""
Crie um programa onde o usúario decide qual esquação ele deseja calcular: equação do 1º grau ou equação do 2º grau
"""
    
import os
import math #math.sqrt(valor)

def exibir_menu():
    print("Digite 1 para calcular uma equação do 1º grau:")
    print("Digite 2 para calcular uma equação do 2º grau:")
    print("Digite 3 para sair do programa")

def equacao_1(a,b):
    equacao_primeiro_grau = (a * x) + b
    return equacao_primeiro_grau
def equacao_2(a,b,c):
    if a == 0:
        return equacao_2(a,b,c)
    else:
        equacao_segundo_grau = (b**2) - 4*a*c
    if equacao_segundo_grau < 0:
        return("Como delta é menor que zero, não existe raiz real. Portanto, não existe x1 e x2.")
    elif equacao_segundo_grau == 0:
        x = -b/(2*a)
        return(f"O resultado da equação do primeiro grau é {x}")
    else:
        x1 = (-b + match.sqrt(equacao_segundo_grau) / (2*a))
        x2 = (-b - match.sqrt(equacao_segundo_grau) / (2*a))
        return(f"Os resultados são: x1={x1} e x2={x2}")

while True:
    exibir_menu()
    opcao = input("Digite o número da equação que você deseja resolver:")

    os.system("cls")

    if opcao == "1":
        a = int(input("Informe o valor de a:"))
        b = int(input("Informe o valor de b:"))
        print(f"O resultado da equação do primeiro grau é {equacao_1(a, b)}")
    elif opcao == "2":
        a = int(input("Informe o valor de a:"))
        b = int(input("Informe o valor de b:"))
        c = int(input("Informe o valor de c:"))
        resposta = equacao_2(a,b,c)
        print(resposta)
    elif opcao == "3":
        print("Você saiu do programa. Volte sempre!")
    else:
        print("Opção invalida!")