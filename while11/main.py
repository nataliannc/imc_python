#importa as bibliotecas
import os
import time

contador = int(input("Informe um número inteiro:"))
#permite acessar o promp de comando
os.system('cls')

#conta a partir do número informado até 0
#-= -> subtrai a um valor e atribui o resultado

while contador >= 0:
    print(f'Contagem regressiva: {contador}')
    time.sleep(100) #função da biblioteca time: mostra a contagem de 1 em 1 segundo
    os.system('cls')
    contador -= 1

print("BOOOM!!!")