#recebe o nome do usuário 
nome = input("informe o seu nome:")

#exibe a lista de filmes e suas salas
print("LISTA DE FILMES\n")
print("Sala 1 - A volta dos que não foram")
print("Sala 2 - A roda quadrada")
print("Sala 3 - Poeira em alto mar")
print("Sala 4 - As tranças do rei careca")
print("Sala 5 - A vingança do peixe frito")

#recebe a sala escolhida
sala = int(input("informe a sala desejada:"))

match sala: 
    case 1: 
        print(f"Filme escolhido por {nome}: A volta dos que não foram")
    case 2:
        print(f"Filme escolhido por {nome}: A roda quadrada")
    case 3:
        print(f"Filme escolhido por {nome}: Poeira em alto mar")
    case 4:
        print(f"Filme escolhido por {nome}: As tranças do rei careca")
    case 5:
        print(f"Filme escolhido por {nome}: A vingança do peixe frito")
    case _:
        print("Sala inexistente.")