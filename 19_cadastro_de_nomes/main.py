#lista de frutas
frutas = ["maracujá", "banana", "maçã"]

#usuário informa o nome da nova fruta
nova_fruta = input("Informe o nome de uma fruta:")

#nova fruta é inserida na lista / append = acrescentar
frutas.append(nova_fruta)

#exibe na tela a nova lista
for fruta in frutas:
    print(fruta)
