#instalar biblioteca pip install forex-python
#executar comando para verificar bibliotecas que estão no projeto pip freeze > requirements.txt

from forex_python.converter import CurrencyRates

valor = str(input("Informe o valor da moeda a ser convertida:")).replace(',','.')
valor = float(valor)
moeda_origem = input("Informe a moeda de origem:").upper()
moeda_destino = input("Informe a moeda de destino:").upper()

#faz a conversão de acordo com a taxa de câmbio do dia
result = CurrencyRates().convert(moeda_origem, moeda_destino, valor)

#exibe o resultado na tela
print(f"${valor:,2f} {moeda_origem} = ${result:,.2f} {moeda_destino}.")