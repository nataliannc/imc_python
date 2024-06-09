import os

lista_de_tarefas = []

while True:

    #menu apresentado para o usúario
    print(f"{'='*20} AÇÕES DISPONÍVEIS {'='*20}\n")
    print("Adicionar uma nova tarefa: DIGITE 1")
    print("Visualizar todas as tarefas: DIGITE 2")
    print("Marcar uma tarefa como concluída: DIGITE 3")
    print("Remover uma tarefa: DIGITE 4")
    print("Sair do programa: DIGITE 5")
    print(f"{'='*60}")

    opcao_usuario = input("Informe a opção desejada:")

    os.system("cls")

    #cadastrar tarefa
    if opcao_usuario == "1":
        tarefa = input("Informe uma tarefa:")
        lista_de_tarefas.append(tarefa)
        print("Tarefa adicionada!")

    #visualizar tarefas
    elif opcao_usuario == "2":
        for tarefa in lista_de_tarefas:
            print(tarefa)

    #concluir tarefa
    elif opcao_usuario == "3":
        tarefa_para_atualizar = input("Informe a tarefa concluida:")
        if tarefa_para_atualizar in lista_de_tarefas:
            index = lista_de_tarefas.index(tarefa_para_atualizar)
            lista_de_tarefas[index] = tarefa_para_atualizar + " - tarefa concluida"
            print("Tarefa concluida.")
        else:
            print("Tarefa não encontrada.")

    #deletar tarefa
    elif opcao_usuario == "4":
        tarefa = input("Informe a tarefa a ser deletada:")
        if tarefa in lista_de_tarefas:
            lista_de_tarefas.remove(tarefa)
            print("Tarefa deletada.")
        else:
            print("Tarefa não encontrada.")

    #sair do programa
    elif opcao_usuario == "5":
        print("Você saiu do programa. Volte sempre!")
        break

    #opção inválida
    else:
        print("Opção inválida.")