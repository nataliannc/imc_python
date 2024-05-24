nomes = ["Ana", "Bia", "Diego", "Ellen", "Fran", "Elsa"]

#usuário informa o indice que deseja alterar
indice = int(input("Informe o índice que deseja altarar:"))
indice -= 1

#usuário informa o novo nome
nomes[indice] = input("Informe o novo nome:")

#exibe a lista
for nome in nomes:
    print(nome)