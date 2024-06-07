#lambda é usado para simplificar uma função

calcular_retangulo = lambda base, altura: base * altura

base = int(input('Informe a base do rêtangulo:'))
altura = int(input('Informe a altura do retângulo:'))

print(f'A área do retângulo é {calcular_retangulo(base, altura)}')