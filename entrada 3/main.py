# entrada de dados e saída de dados

nome = input("informe o seu nome:")
print (f"Meu nome é {nome}.")

#replace irá converter , por .
altura = str(input("informe a sua altura:")).replace(',','.')
print (f"A sua altura é: {altura}")

#converter str para float
altura = float(altura)

#saída de dados
print(f"Meu nome é {nome} e tenho {altura} metros de altura.")