"""
calculadora feita em python
que recebe dois números e calcula a operação desejada 
pelo usúario
"""
while True: #loop infinito

    n1 = str(input("Digite o primeiro número:")).replace(',','.')
    n2 = str(input("Digite o segundo número:")).replace(',','.')

    n1 = float(n1)
    n2 = float(n2)

    print('Operações:')
    print('"/" divisão')
    print('"+" soma')
    print('"-"subtração')
    print('"*" multiplicação')
    print('"%" resto')

    operacao = input(("Qual operação você deseja realizar?"))

    match operacao:
        case '+':
            print(f"A soma é: {n1 + n2}")
        case '-':
            print(f"A subtração é: {n1 - n2}")
        case '*':
            print(f"A multiplicação é: {n1 * n2}")
        case '/':
            print(f"A divisão é: {n1 / n2}")
        case '%':
            print(f"O resto da divisão é: {n1 % n2}")
        case _:
            print("Operação inválida")
            continue #interrompe o loop na linha de comando e volta para o inicio do proximo loop
        
    #PERGUNTA PARA O USUÁRIO SE DESEJA CONTINUAR OU ENCERRAR
    continuar = input("Deseja continuar (s/n)?")

    #verifica a opção do usuário
    if continuar == "s":
        continue #volta para o inicio do proximo loop
    elif continuar == "n":
        break #interrompe o loop de forma definitiva
    else:
        print("Opção inválida")
        continue