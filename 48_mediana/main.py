"""
INCOMPLETO
"""

"""
Crie um programa que cadastre o nome de 30 alunos em uma lista, e receba de cada aluno 5 notas de 0 a 10. 
O programa deverá retornar a média do aluno e indicar se o aluno está aprovado ou reprovado (média para aprovação = 7). 
Ao final, o programa deverá mostrar uma lista com o nome dos aprovados.
"""

alunos = []

while True:

    #menu apresentado para o usúario
    print(f"{'='*20} AÇÕES DISPONÍVEIS {'='*20}\n")
    print("Cadastrar aluno: DIGITE 1")
    print("Adicionar nota de um aluno cadastrado: DIGITE 2")
    print("Visualizar alunos cadastrados: DIGITE 3")
    print("Sair do programa: DIGITE 4")
    print(f"{'='*60}")

    opcao_usuario = input("Informe a opção desejada:")

    #cadastrar alunos
    if opcao_usuario == "1":
        aluno = input("Informe o nome de um aluno:")
        # nota_aluno1 = input("Informe a 1ª nota do aluno:")
        # nota_aluno2 = input("Informe a 2ª nota do aluno:")
        # nota_aluno3 = input("Informe a 3ª nota do aluno:")
        # nota_aluno4 = input("Informe a 4ª nota do aluno:")
        # nota_aluno5 = input("Informe a 5ª nota do aluno:")
        # alunos.append(aluno)
        # alunos.append(nota_aluno1)
        # alunos.append(nota_aluno2)
        # alunos.append(nota_aluno3)
        # alunos.append(nota_aluno4)
        # alunos.append(nota_aluno5)
        print("Aluno adicionado!")

    #concluir tarefa
    elif opcao_usuario == "2":
        adicionar_nota_aluno = input("Informe o nome do aluno para acidionar as notas:")
        if adicionar_nota_aluno in alunos:
            nota_aluno1 = input("Informe a 1ª nota do aluno:")
            nota_aluno2 = input("Informe a 2ª nota do aluno:")
            nota_aluno3 = input("Informe a 3ª nota do aluno:")
            nota_aluno4 = input("Informe a 4ª nota do aluno:")
            nota_aluno5 = input("Informe a 5ª nota do aluno:")
            index = alunos.index(nota_aluno1, nota_aluno2, nota_aluno3, nota_aluno4, nota_aluno5)
            alunos[index] = adicionar_nota_aluno + nota_aluno1
        else:
            print("Aluno não encontrada.")

    #visualizar alunos
    elif opcao_usuario == "3":
        for aluno in alunos:
            print(aluno)

    #sair do programa
    elif opcao_usuario == "4":
        print("Você saiu do programa. Volte sempre!")
        break

    #opção inválida
    else:
        print("Opção inválida.")
