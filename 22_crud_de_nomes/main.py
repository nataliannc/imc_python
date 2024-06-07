#crud = sistemas que fazem 4 operações -> cadastrar...
'''
crie um programa que tenha as opções:
    - cadastrar(inserir) pessoa na lista
    - listar pessoas cadastradas
    - pesquisar pelo nome de uma pessoa
    - ordenar a lista por ordem alfabética
    - atualizar nome
    - deletar nome da lista
    - sair do programa
'''

lista_de_nomes = []

while True:

    print(f"{'='*20} AÇÕES DISPONÍVEIS {'='*20}\n")
    print("Cadastrar/inserir nome: DIGITE 1")
    print("Listar nomes cadastrados: DIGITE 2")
    print("Pesquisar nomes: DIGITE 3")
    print("Ordenar a lista por ordem alfabética: DIGITE 4")
    print("Atualizar nome: DIGITE 5")
    print("Deletar nome: DIGITE 6")
    print("Sair do programa: DIGITE 7")
    print(f"{'='*60}")

    opcao_usuario = input("Informe a opção desejada:")

    #cadastrar nome
    if opcao_usuario == "1":
        nome = input("Informe um nome para cadastrar:")
        lista_de_nomes.append(nome)
        print("Nome cadastrado!")

    #listar nomes da lista
    elif opcao_usuario == "2":
        for nome in lista_de_nomes:
            print(nome)

    #pesquisar nomes na lista
    elif opcao_usuario == "3":
        nome = input("Informe o nome a ser pesquisado:")
        if nome in lista_de_nomes:
            print("Nome encontrado na lista.")
        else:
            print("Nome não encontrado na lista.")

    #ordenar a lista por odem alfabética
    elif opcao_usuario == "4":
        lista_de_nomes.sort()
        for nome in lista_de_nomes:
            print(nome)

    #atualizar nomes da lista
    elif opcao_usuario == "5":
        nome_para_atualizar = input("Informe o nome a ser alterado:")
        if nome_para_atualizar in lista_de_nomes:
            nome_atualizado = input("Informe o novo nome:")
            index = lista_de_nomes.index(nome_para_atualizar)
            lista_de_nomes[index] = nome_atualizado
            print("Nome atualizado.")
        else:
            print("Nome não encontrado.")

    #deletar nomes da lista
    elif opcao_usuario == "6":
        nome = input("Informe o nome a ser deletado:")
        if nome in lista_de_nomes:
            lista_de_nomes.remove(nome)
            print("Nome deletado.")
        else:
            print("Nome não encontrado.")

    #sair do programa
    elif opcao_usuario == "7":
        print("Você saiu do programa. Volte sempre!")
        break

    #opção inválida
    else:
        print("Opção inválida.")
