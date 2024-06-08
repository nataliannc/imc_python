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
import os
from datetime import date

campos = ("Nome")
cadastros = []

while True:

    print(f"{'*'*20} AÇÕES DISPONÍVEIS {'*'*20}\n")
    print("Cadastrar nome: DIGITE 1")
    print("Deletar nome: DIGITE 2")
    print("Entrar no aplicativo: DIGITE 3")
    print(f"\n{'*'*59}")

    opcao_usuario = input("Informe a opção desejada:")

    os.system("cls")

    #cadastrar pessoa
    if opcao_usuario == "1":
        print("Informe os dados abaixo:")
        nome = input("Informe o seu nome:")
        pessoa = (nome)
        cadastros.append(pessoa)
        print("Pessoa cadastrada!")

    #deletar nome da lista
    elif opcao_usuario == "2":
        pessoa_deletada = input("Informe o nome da pessoa a ser deletado:")
        try:
            cadastros.remove(pessoa_deletada)
            print("Nome deletado!")
        except:
            print("Não foi possível deletar o nome informado. Informe um nome existente.")

    #entrar no aplicativo
    elif opcao_usuario == "3":
        while True:
            print(f"{'*'*20} AÇÕES DISPONÍVEIS {'*'*20}\n")
            print("Consultar saldo: DIGITE 1")
            print("Depositar valor: DIGITE 2")
            print("Sacar valor: DIGITE 3")
            print("Sair do programa: DIGITE 4")
            print(f"\n{'*'*59}")

            opcao_usuario_surfing = input("Informe a opção desejada:")

            os.system("cls")

            #consultar saldo
            if opcao_usuario_surfing == "1":
                print("Informe os dados abaixo:")
                cpf = input("Informe o seu CPF:")
                telefone = input("Informe um número de telefone:")
                email = input("Informe o seu e-mail:")
                pessoa = (cpf, telefone, email)
                cadastros.append(pessoa)
                print("\nConta criada com sucesso!")

                meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

                dia = date.today().day
                mes = date.today().month
                ano = date.today().year

                print(f"\n{dia} de {meses[mes - 1]} de {ano}. \n")
                print(f"O seu saldo é: {novo_saldo}\n")
                
            #depositar valor
            elif opcao_usuario_surfing == "2":
                novo_saldo = input("Informe o valor a ser depositado:")
                saldo = (novo_saldo)
                cadastros.append(saldo)
                for valor in novo_saldo:
                    somas = [valor + val for val in novo_saldo]
                print(f"Seu saldo é: {novo_saldo}")

            #sacar valor
            elif opcao_usuario_surfing == "3":
                print()

            #sair do programa
            elif opcao_usuario_surfing == "4":
                print("Você saiu do programa. Volte sempre!")
                break

            #opção inválida
            else:
                print("Opção inválida.")

    #opção inválida
    else:
        print("Opção inválida.")