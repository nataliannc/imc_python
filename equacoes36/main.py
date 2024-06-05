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
    if a == 0:
        if b == 0:
            return "A equação é indeterminada."
        else:
            return "A equação não tem solução."
    else:
        x = -b/a
        return f"O resultado é: x= {x}"
def equacao_2(a,b,c):
    if a == 0:
        return equacao_1(b,c)
    else:
        equacao_segundo_grau = (b**2) - 4*a*c
    if equacao_segundo_grau < 0:
        return "Como delta é menor que zero, não existe raiz real. Portanto, não existe x1 e x2."
    elif equacao_segundo_grau == 0:
        x = -b/(2*a)
        return f"O resultado da equação do primeiro grau é {x}"
    else:
        x1 = (-b + match.sqrt(equacao_segundo_grau) / (2*a))
        x2 = (-b - match.sqrt(equacao_segundo_grau) / (2*a))
        return f"Os resultados são: x1={x1} e x2={x2}"

while True:
    exibir_menu()
    opcao = input("Digite a opção desejada:")

    os.system("cls")

    if opcao == "1":
        a = float(input("Informe o valor de a:"))
        b = float(input("Informe o valor de b:"))
        resposta = equacao_1(a,b)
        print(resposta)
    elif opcao == "2":
        a = float(input("Informe o valor de a:"))
        b = float(input("Informe o valor de b:"))
        c = float(input("Informe o valor de c:"))
        resposta = equacao_2(a,b,c)
        print(resposta)
    elif opcao == "3":
        print("Você saiu do programa. Volte sempre!")
    else:
        print("Opção invalida!")