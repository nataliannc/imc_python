"""
Crie um CRUD utilizando os conceitos de lista, tupla e dicionário. 
O usuário pode cadastrar quantas pessoas quiser. 
Os dados a serem cadastrados são:
- Nome
- CPF
- Telefone
- E-mail
- Profissão
- Empresa

CRUD = cadastrar, listar, alterar, deletar e (sair do programa)
"""

#lista de dicionário
campos = ("Nome", "CPF", "Telefone")
pessoas = []

while True:

    print(f"{'█'*20} AÇÕES DISPONÍVEIS {'█'*20}\n")
    print("Cadastrar nomes: DIGITE 1")
    print("Listar nomes cadastrados: DIGITE 2")
    print("Alterar nome: DIGITE 3")
    print("Deletar nome: DIGITE 4")
    print("Sair do programa: DIGITE 5")
    print(f"{'█'*59}")

    opcao_usuario = input("Informe a opção desejada:")

    #cadastrar pessoa
    if opcao_usuario == "1":
        print("Informe os dados abaixo:")
        nome = input("Informe o nome:")
        cpf = input("Informe o CPF:")
        telefone = input("Informe o telefone:")
        email = input("Informe o e-mail:")
        profissao = input("Informe a profissão:")
        empresa = input("Informe a empresa:")
        pessoa = (nome, cpf, telefone, email, profissao, empresa)
        pessoas.append(pessoa)
        print("Pessoa cadastrada!")

    #listar pessoa cadastradas
    elif opcao_usuario == "2":
        print(pessoas.get(nome))
        print(pessoas.get(cpf))
        print(pessoas.get(telefone))
        print(pessoas.get(email))
        print(pessoas.get(profissao))

    #deletar nomes da lista
    elif opcao_usuario == "4":
        del pessoas[input('Informe a chave que deseja excluir: ')]

    #sair do programa
    elif opcao_usuario == "5":
        print("Você saiu do programa. Volte sempre!")
        break

    #opção inválida
    else:
        print("Opção inválida.")
