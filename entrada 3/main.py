# entrada de dados e saída de dados

nome = input("informe o seu nome:")
print (f"Meu nome é {nome}.")

#replace irá converter , por .
altura = str(input("informe o seu peso:")).replace(',','.')
print (f"O seu peso é {altura}")


#converter str para float
altura = float(altura)

#saída de dados
print(f"Meu nome é {nome} e tenho {altura} metros de altura.")


