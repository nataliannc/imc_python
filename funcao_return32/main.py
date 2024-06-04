# função que calcula a area de um rêtangulo
def calcular_retangulo(base, altura):
    area = base * altura
    return area

# programa principal
base = int(input('Informe a base do rêtangulo:'))
altura = int(input('Informe a altura do retângulo:'))

print(f'A área do retângulo é {calcular_retangulo(base, altura)}')