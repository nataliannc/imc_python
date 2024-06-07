"""
INCOMPLETO
"""

"""
Crie um aplicativo de banco, onde o usuário possa:

- Cadastrar seu nome no aplicativo.
- Deletar seu nome do aplicativo.
- Entrar no aplicativo.

Ao entrar no aplicativo, o usuário pode:

- Consultar seu saldo (criar uma nova conta o saldo começa com R$ 0,00; a consulta deverá exibir a data da consulta)
- Depositar valor.
- Sacar valor.
- Sair do programa.

Ao terminar, envie para o GitHub e poste o link.
"""

campos = ("Nome")
pessoas = []

while True:

    print(f"{'*'*20} AÇÕES DISPONÍVEIS {'*'*20}\n")
    print("Cadastrar nome: DIGITE 1")
    print("Deletar nome: DIGITE 2")
    print("Entrar no aplicativo: DIGITE 3")
    print(f"\n{'*'*59}")

    opcao_usuario = input("Informe a opção desejada:")

    #cadastrar pessoa
    if opcao_usuario == "1":
        print("Informe os dados abaixo:")
        nome = input("Informe o nome:")
        pessoa = (nome)
        pessoas.append(pessoa)
        print("Pessoa cadastrada!")

    #deletar nomes da lista
    elif opcao_usuario == "2":
        pessoa_deletada = input("Informe o nome da pessoa a ser deletado:")
        try:
            pessoas.remove(pessoa_deletada)
            print("Nome deletado!")
        except:
            print("Não foi possível deletar o nome informado. Informe um nome existente.")

    #entrar no aplicativo
    elif opcao_usuario == "3":
        