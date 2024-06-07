#importa o módulo
from modulo import *
import os
#para importar apenas uma função: from modulo import calcular_circulo

if __name__ == "__main__":
    while True:
        exibir_menu()
        opcao = input("Opção desejada:")

        os.system("cls")

        match opcao:
            case "1":
                b = int(input("Informe o valor da base:"))
                h = int(input("Informe o valor da altura:"))
                print(f"Área do quadrilátero: {calcular_quadrilatero(b,h)}.")
                continue
            case "2":
                r = int(input("Informe o valor do raio:"))
                print(f"Área do círculo: {calcular_circulo(r)}.")
                continue
            case "3":
                b = int(input("Informe o valor da base do triângulo:"))
                h = int(input("Informe o valor da altura do triângulo:"))
                print(f"Área do triãngulo: {calcular_triangulo(b,h)}.")
                continue
            case "4":
                base1 = int(input("Informe o valor da primeira base do trapézio:"))
                base2 = int(input("Informe o valor da segunda base do trapézio:"))
                h = int(input("Informe o valor da altura do trapézio:"))
                print(f"Área do trapézio: {calcular_trapezio(base1, base2, h)}.")
                continue
            case "5":
                break